from gtts import gTTS
from art import tprint
from pathlib import Path
from pdfreader import SimplePDFViewer

def pdf_to_mp3(file_path="questions.pdf", language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'Original file: {Path(file_path).name}')

        print('Process')

        with open(file_path, 'rb') as pdf_file:
            viewer = SimplePDFViewer(pdf_file)
            text = ''
            for canvas in viewer:
                if canvas.strings:
                    text += ''.join(canvas.strings)

        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)

        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 saved'

    else:
        return 'File does not exist check the file path'

def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')

    file_path = input("\nEnter a file's path: ")
    language = input("Choose language en or ru: ")

    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()
