from SublimeLinter.lint import Linter, util  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class Soar(Linter):
    cmd = 'soar -report-type lint -query'
    multiline = True
    tempfile_suffix = 'sql'
    regex = (
        r'(?P<message>.+$(?:\r?\n  .+$)*)'
    )


    line_col_base = (1, 1)
    output_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'source.sql'
    }


    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        message = message.split(":")[-1]
        line = 1
        print(match, line, col, error, warning, message, near)
        return  match, line, col, error, warning, message, near