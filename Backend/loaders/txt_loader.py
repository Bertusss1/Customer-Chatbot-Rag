from pathlib import Path


def load_txt(folder):

    documents = []

    for file in Path(folder).glob("*.txt"):

        with open(
            file,
            encoding="utf-8"
        ) as f:

            documents.append({

                "source": file.name,

                "type": "txt",

                "text": f.read()

            })

    return documents