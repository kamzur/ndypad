#!/usr/bin/python
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
class NdyPad:
	
	curren_file = ''
	def __init__(self,tk):
		self.root = tk
		self.root.geometry("500x500")
		self.root.title("Ndypad v 1.0 " + self.curren_file)

		# disabled resize window
		self.root.resizable(40,40)
		# define options for opening or saving a files
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		options['initialfile'] = ''
		options['parent'] = self.root
		options['title'] = 'This is a title'
		
		# define options for saving file only
		self.file_saveas_opt = options_save = {}
		options_save['defaultextension'] = '.txt'
		options_save['filetypes'] = [('all files', '.*'), ('text files', '.*')]
		options_save['initialdir'] = 'D:\\'
		if self.curren_file == '':
			options_save['initialfile'] = ''
		else:
			options_save['initialfile'] = self.curren_file
		options_save['parent'] = self.root
		options_save['title'] = 'This is a title'
		
		self.buat_text()
		
		# sortcut
		self.buat_key_saveas()
		self.buat_key_open()
		self.buat_key_simpan()
		
		# pack and configure 
		# text widget
		self.buat_scroll()
		self.text.pack(side=LEFT, fill=Y)
		
		# buat status bar:
		self.buat_statusbar()
		
		self.text.config(yscrollcommand=self.scroll.set)
		
		self.buat_menu()
		
	def buat_menu(self):
		# buat objek menubar
		menubar = Menu(self.root)
		
		# buat menu 'file'
		menufile = Menu(menubar, tearoff=0)
		menufile.add_command(label="New")			# tambah New
		menufile.add_command(label="Open..",command=self.buka_file)						# tambah Open
		menufile.add_command(label="Save",command=self.simpan_asfile)					# tambah Save
		menufile.add_command(label="Save As..",command=self.simpan_asfile)	# tambah Save Ass
		menufile.add_separator()					# separator ----
		menufile.add_command(label="Exit")			# tambah Exit
		
		# start menu 'file'
		menubar.add_cascade(label="File", menu=menufile)
		self.root.config(menu=menubar)
		
	def buat_text(self):
		# objek text
		self.text = Text(self.root, height=500,width=500,bg="black", fg="white")
		
	def buka_file(self, event=None):
		self.filename = tkFileDialog.askopenfilename(**self.file_opt)
		self.curren_file = self.filename.encode('utf-8')
		self.root.title("Ndypad v 1.0 " + self.curren_file)
		self.baca_file_text()
		
	def baca_file_text(self):
		if self.filename:
			# panggil method hapus_text
			# sebelum membuka dan membaca file
			self.hapus_text()
			file = open(self.filename,"r")
			self.text.insert(INSERT, file.read())
			
	def hapus_text(self):
		# method buat ngapus string
		# di widget text
		self.text.delete('0.0',END)
		
	def simpan_file(self, event=None):
		# method ini buat
		# nyimpen file
		self.savefile = tkFileDialog.asksaveasfilename(**self.file_saveas_opt)
		
		# dari unicode convert ke String
		# yang diubah ke utf-8 menjadi string
		data_encoded = self.ambil_text().encode('utf-8')
		
		# memulai penulisan file
		save = open(self.savefile, 'w')
		self.curren_file = save.name
		self.file_saveas_opt['initialfile'] = save.name
		save.write(data_encoded)
		save.close()
		
	def simpan_asfile(self,event=None):
		# method ini buat
		# nyimpen file
		self.savefile = tkFileDialog.asksaveasfilename(**self.file_saveas_opt)
		
		# dari unicode convert ke String
		# yang diubah ke utf-8 menjadi string
		data_encoded = self.ambil_text().encode('utf-8')
		
		# memulai penulisan file
		save = open(self.savefile, 'w')
		save.write(data_encoded)
		save.close()
		
	def buat_scroll(self):
		# method ini digunakan
		# untuk membuat scroll
		self.scroll = Scrollbar(self.root)
		self.scroll.pack(side=RIGHT, fill=Y)
		self.scroll.config(command=self.text.yview)
		
	def buat_statusbar(self):
		# mrthod ini digunakan untuk
		# membuat status bar <not work>
		self.var_statusbar = StringVar()
		self.statusbar = Label(self.root, bd=1, relief=SUNKEN,\
		anchor=W, textvariable=self.var_statusbar)
		self.var_statusbar.set("Status Bar")
		self.statusbar.pack(fill=X)
		
	def buat_key_simpan(self):
		# method untuk mendefinisikan
		# key binding event penyimpanan file
		# dengan cara menekan Control-S
		self.root.bind('<Control-s>', self.simpan_file)
		
	def buat_key_saveas(self):
		# method untuk mendefinisikan
		# key binding event penyimpanan asfile
		# dengan cara menekan Control+Space+S
		self.root.bind('<Control-d>', self.simpan_asfile)
		
	def buat_key_open(self):
		# method untuk mendefinisikan
		# key binding event open file
		# dengan cara menekan Control+O
		self.root.bind('<Control-o>', self.buka_file)
		
	def ambil_text(self):
		return self.text.get("0.0",END)
		
		