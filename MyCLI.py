from openai import OpenAI
import cmd
class MyCLI(cmd.Cmd):
    intro = 'welcome to shabbu cli'
    prompt='(shabbu) '
    file = None

    def do_summarize(self, line):
        client = OpenAI(api_key="api_key")
        summary = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role":"user", "content":"you are tasked with summarising the given text {0} in bullet points".format(line)}])
        print(summary.choices[0].message.content.strip())
    def do_quit(self, line):
        print('fare thee well, sire!')
        """Exit the CLI"""
        return True
    def precmd(self, line):
        print('I am just about to run your command')
        return line
    def postcmd(self, stop, line):
        print('your command must have run by now!')
        return super().postcmd(stop, line)
    
    
if __name__ == '__main__':
    MyCLI().cmdloop()


