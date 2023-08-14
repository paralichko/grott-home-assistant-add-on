# use pydoit to run the pipeline
# url: http://pydoit.org/
# install pydoit: pip install doit (or pipx)

import os
import glob

BUILDS = [
    "grott",
    "grott-current",
]

TRANSLATIONS_FOLDER = "translations"


def task_copy_translations():
    """Copy translations from the source to the translations folder."""
    translations = glob.glob(f"{TRANSLATIONS_FOLDER}/*.yaml")

    for build in BUILDS:
        for translation in translations:
            # get the file basename
            translation = os.path.basename(translation)
            yield {
                "name": f"copy {translation} to {build}",
                "actions": [
                    f"mkdir -p {build}/translations",
                    f"cp {TRANSLATIONS_FOLDER}/{translation} {build}/translations/{translation}",
                ],
                "file_dep": [f"{TRANSLATIONS_FOLDER}/{translation}"],
                "targets": [f"{build}/translations/{translation}"],
            }

def task_copy_requirements():
    """Copy requirements.txt to the builds."""
    for build in BUILDS:
        yield {
            "name": f"copy requirements.txt to {build}",
            "actions": [
                f"cp requirements.txt {build}/requirements.txt",
            ],
            "file_dep": ["requirements.txt"],
            "targets": [f"{build}/requirements.txt"],
        }
