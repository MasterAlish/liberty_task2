import bonobo

from loaders.sqlite import ProgramToSqlite
from readers.file_reader import FilesReader
from transforms.xml import ProgramXmlParser

if __name__ == '__main__':
    graph = bonobo.Graph(
        FilesReader("ingest"),
        ProgramXmlParser(),
        ProgramToSqlite()
    )

    bonobo.run(graph)
