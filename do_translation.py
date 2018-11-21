from py_translator import Translator
import taglib
import os
import re

if __name__ == "__main__":
    translator = Translator()

    for root, dirs, files in os.walk("input"):
        for file in files:
            full_dir_in = os.path.join(root, file)
            if os.path.splitext(file)[1] in [".mp3", ".m4a"]:
                print("Working on %s..." % full_dir_in)
                song = taglib.File(full_dir_in)
                for field in ["ARTIST", "ALBUM", "TITLE"]:
                    if field in song.tags.keys():
                        for i, entry in enumerate(song.tags[field]):
                            translated = translator.translate(entry)
                            song.tags[field][i] = translated.text
                song.save()
                # And then rename the file itself
                base, ext = os.path.splitext(file)
                translated_base = translator.translate(base).text
                full_dir_out = os.path.join(root, translated_base + ext)
                print("Dumping to full file %s" % full_dir_out)            
                os.rename(full_dir_in, full_dir_out)