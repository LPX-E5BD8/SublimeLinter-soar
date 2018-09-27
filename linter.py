from SublimeLinter.lint import Linter, util, persist  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class Soar(Linter):
    try:
        cmd = persist.settings.get('linters').get('soar').get("soar_path") + " -report-type lint -query"
    except Exception as e:
        cmd = "soar -report-type lint -query"
    
    multiline = True
    
    tempfile_suffix = 'sql'
    regex = (
        r'^.+?:(?P<line>\d+):'
        r'(?P<message>.+$(?:\r?\n  .+$)*)'
    )

    defaults = {
        'selector': 'source.sql'
    }

    line_col_base = (1, 1)
    output_stream = util.STREAM_BOTH

    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        message = message.split(":")[-1]
        col=0
        return  match, line, col, error, warning, message, near