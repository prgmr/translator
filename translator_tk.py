#!/usr/bin/python3
# -*- coding: utf-8 -*-


def output(event):
	tr_text = entry.get(1.0,END)
	s = tr_engine.get()
	if s == 1: google(tr_text)
	elif s == 2: yandex(tr_text)
	elif s == 3: microsoft(tr_text)


def google(text):
	import goslate
	gs = goslate.Goslate()
	lang = gs.detect(text)
	print(lang)

	if lang == "en":
		h = gs.translate(text, 'ru')
	elif lang == "ru":
		h = gs.translate(text, 'en')
	print(h)

	outtext.delete(1.0,END)
	outtext.insert(END,h)


def yandex(text):
	from yandex_translate import YandexTranslate
	translate = YandexTranslate('<YANDEX-API-KEY>')
	lang = translate.detect(text)

	outtext.delete(1.0,END)

	# весь текст перевести в нижний регистр и разделить по пробелам в список
	# и удалить символы ! и ?
	words = text.lower().translate({ord('!'): '', ord('?'): ''}).split()

	# убрать повторяющиеся слова (преобразовав в кортеж) и отсортировать по алфавиту
	words = sorted(set(words))





	for word in words:

		if lang == "en":
			h = translate.translate(word, 'en-ru')
		elif lang == "ru":
			h = translate.translate(word, 'ru-en')

		outtext.insert(END, word + " - " + str(h.get("text")) + "\n")


from tkinter import *

root = Tk()
root.title("RU/ENG automate Translator")
tr_engine = IntVar()
tr_engine.set(2)

hello = Label(root, text="Введите текст или слово для перевода: ")
entry = Text(root,width=100, height=20)
translater = Label(root, text="Выберите движок для перевода: ")
R1 = Radiobutton(root, text="google translate", padx = 20, variable=tr_engine, value=1)
R2 = Radiobutton(root, text="yandex translate", padx = 20, variable=tr_engine, value=2)
button = Button(root,text="перевести")
outtext = Text(root,width=100,height=20,wrap=WORD)


hello.pack()
entry.pack()
entry.focus_set()
translater.pack()
R1.pack(anchor=W)
R2.pack(anchor=W)
button.pack()
outtext.pack()


root.bind("<Return>",output)
button.bind("<Button-1>",output)

root.mainloop()
