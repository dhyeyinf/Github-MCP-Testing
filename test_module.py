
def get_code_execution_tools(self) -> Optional[List[BaseTool]]:
        """
        Retrieve tools for code execution, based on the agent's execution mode.

        Returns:
            List[BaseTool] | None: List of code execution tools if available,
            otherwise None if crewai_tools is not installed.
        """
