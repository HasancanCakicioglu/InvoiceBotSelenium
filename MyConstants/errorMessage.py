from MyConstants.enum import prgoramProcess

errorMessageBox = ""

class ProgramProcessHandler:
    process_handler = prgoramProcess.Start.value

    @staticmethod
    def set_process_handler(programProcess : prgoramProcess):
        ProgramProcessHandler.process_handler = programProcess.value

    @staticmethod
    def get_process_handler() -> str:
        return ProgramProcessHandler.process_handler

class GibProcessHandler:
    gib_process_handler = prgoramProcess.Start.value

    @staticmethod
    def set_process_handler(programProcess : prgoramProcess):
        GibProcessHandler.gib_process_handler = programProcess.value

    @staticmethod
    def get_process_handler() -> str:
        return GibProcessHandler.gib_process_handler

