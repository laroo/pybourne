import sys
import time
import asyncio
from asyncio.subprocess import PIPE
from pybourne import info, error


class ShellCommand(object):

    def __init__(self, cmd):
        self.cmd = cmd
        self.return_code = None

    async def _copy_stream(self, stream, output_type=1):
        """ Read from stream line by line until EOF, copying it to outfile. """
        while True:
            line = await stream.readline()
            if not line:
                break

            if output_type == 1:
                info(line)
            else:
                error(line)

    async def _run_and_pipe(self):
        process = await asyncio.create_subprocess_shell(self.cmd, stdout=PIPE, stderr=PIPE)

        try:
            await asyncio.gather(
                self._copy_stream(process.stdout, output_type=1),
                self._copy_stream(process.stderr, output_type=2)
            )
        except Exception as e:
            process.kill()
            raise e
        finally:
            # wait for the process to exit
            rc = await process.wait()
        return rc

    def run(self):
        loop = asyncio.get_event_loop()
        self.return_code = loop.run_until_complete(self._run_and_pipe())
        loop.close()
        return self.return_code
