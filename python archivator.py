import os
root_dir=os.listdir()

#нахуй оно надо?
#эта параша нужна что-бы записывать все py и txt файлы в 1 файл
#нахуя?
#да что-бы блять можно было без ебли на питон анвере закидвать большое-кол-во файлов
#кста оно крашится если вы картинки записывать будете
def readFF(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None


def createFF(x,y):
    file = open(str(x), "w", encoding="utf-8")
    file.write(str(y))
    file.close()

def addFF(x,y):
    file = open(str(x), "a", encoding="utf-8")
    file.write(str(y))
    file.close()


print('выберите режим\n1)считать файлы\n2)записать файлы')


mode=input('1,2   ')
print(mode)

mode=='1'
if mode=='1':

	file_name=(os.path.basename(__file__))

	txt_file_info={}
	py_file_info={}
	folder_file_info={}

	print(file_name)
	print()

	createFF('read_files.txt','info_txt={')

	py_files=[]
	txt_files=[]
	folders=[]


	for i in root_dir:
		i=i.lower()
		print(i)
		if i.endswith('.py'):
			py_files.append(i)
		elif i.endswith('.txt'):
			txt_files.append(i)
		elif i.endswith('.ttf'):
			pass
		elif i.endswith('.otf'):
			pass
		else:
			folders.append(i)




	try:
		py_files.remove(file_name)
		folders.remove('__pycache__')
		folders.remove('photos')
	except:
		pass
	txt_files.remove('read_files.txt')
	print('Список нужных директорий получен\n')
	print(f'Убранны файлы \n{file_name}\n__pycache__\nread_files.txt')

	print('\nначат сбор директорий из папок')

	for i in folders:
		dirs=(os.listdir(i))
		for i1 in dirs:
			if i1.endswith('.py'):
				py_files.append(f'{i}/{i1}')
			elif i1.endswith('.txt'):
				txt_files.append(f'{i}/{i1}')
			elif i1.endswith('.ttf'):
				pass
			elif i1.endswith('.otf'):
				pass
			elif i1.endswith('.jpg'):
				pass
			elif i1.endswith('.png'):
				pass
			else:
				folders.append(f'{i}/{i1}')

	print('==================\npy файлы\n')
	print('\n'.join(py_files))
	print('=================')
	print('txt файлы\n')
	print('\n'.join(txt_files))
	print('===========')
	print('папки\n')
	print('\n'.join(folders))


	print('начата запись txt файлов в форме txt')
	addFF('read_files.txt','"txts":'+str(txt_files))
	addFF('read_files.txt',',"txt":{')


	for i in txt_files:

		text=readFF(i)
		txt_file_info[i]=text
	txt_file_info=str(txt_file_info)[1:]
	addFF('read_files.txt',txt_file_info)












	addFF('read_files.txt','}')
	code=readFF('read_files.txt')


	exec(code)










	print('начата запись py файлов в форме txt')
	addFF('read_files.txt','\n\n\ninfo_py={"pys":'+str(py_files))
	addFF('read_files.txt',',"py":{')


	for i in py_files:

		text=readFF(i)
		py_file_info[i]=text
	py_file_info=str(py_file_info)[1:]
	addFF('read_files.txt',py_file_info)


	addFF('read_files.txt','}')
	code=readFF('read_files.txt')


	exec(code)











	print('начата запись папок в форме txt')
	addFF('read_files.txt','\n\n\ninfo_folders={"fols":'+str(folders))


	addFF('read_files.txt','}')
	code=readFF('read_files.txt')


	exec(code)







elif mode=='2':

	code=readFF('read_files.txt')
	exec(code)

	folders_create=info_folders['fols']
	txts_craete=info_txt['txts']
	txt_craete=info_txt['txt']
	pys_craete=info_py['pys']
	py_craete=info_py['py']


	try:


		for i in folders_create:
			os.mkdir(i)
			print('создана папка '+i)
	except:
		pass



	for i in txts_craete:
		text=txt_craete[i]
		createFF(str(i),text)

		print('создан txt файл '+i)



	for i in pys_craete:
		text=py_craete[i]
		createFF(str(i),text)

		print('создан py файл '+i)



print('Процесс завершен')
