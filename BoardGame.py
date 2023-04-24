import sys

file_name = sys.argv[1]
file_name_output = sys.argv[2]
tablo = []
son_tablo = []
puan = 0
sayac=1

#Dosyayı oku
def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

#Tabloyu eski haline getir
def eskiye_cevir(tablo):
    for l in tablo:
        sonuc = ''.join(l)
        son_tablo.append(sonuc)
    return son_tablo

#Dosyaya yaz
def dosyaya_yaz(board):
    dosya = open(file_name_output,"a")
    dosya.write(str(board))

#Tabloyu oluştur
def create_board(board1):
    board = []
    for row in board1.split(','):
        board.append(row)
    return board

#Tabloyu ekrana yazdır
def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()

#Tabloyu oyuna uygun hale getir
def parse_board(board):
    for i in range(0, len(board)):
        tablo.append([])
        for j in range(0, len(board[i])):
            tablo[i].append(board[i][j])
    return tablo

#Oyun bitişini kontrol et
def end_game(board):
    deneme = True
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if i > 0 and board[i][j] == board[i-1][j] and board[i][j] != " ":
                deneme = True
                break
            if i < len(board)-1 and board[i][j] == board[i+1][j] and board[i][j] != " ":
                deneme = True
                break
            if j > 0 and board[i][j] == board[i][j-1] and board[i][j] != " ":
                deneme = True
                break
            if j < len(board[i])-1 and board[i][j] == board[i][j-1] and board[i][j] != " ":
                deneme = True
                break
            else:
                deneme = False
        if deneme == True:
            break
    if deneme == False:
        print_board(kontrol(board))
        print("Oyun bitti")

    return deneme

#oyun başlat
def start_game():
    board=create_board(read_file(file_name)[0])
    parse_board(board)

#Boşlukları kontrol et
def kontrol(board):
    for deneme in range(len(board)-1):
        for i in range(len(board)):
            for j in range(0,len(board[i])-1):
                if board[j+1][i] == ' ':
                    board[j+1][i] = board[j][i]
                    board[j][i] = ' '
    return board

#Hareket
def oyna(board,row,col,main):
    
    if main == ' ':
        print("Boş bir yere hamle yapamazsınız!")
        return
    find_top(board, row, col,main)
    find_left(board, row, col,main)
    find_right(board, row, col,main)
    find_bottom(board, row, col,main)

#üst komşu
def find_top(board, row, col, main):
    global sayac
    if  0 < row:
        if main == board[row-1][col] and main != ' ':
            board[row][col] = ' '
            board[row-1][col] = ' '
            sayac = sayac+1
            row = row-1
            
            return find_top(board, row, col,main),find_left(board, row, col,main),find_right(board, row, col,main),find_bottom(board, row, col,main,)

#alt komşu
def find_bottom(board, row, col, main):
    global sayac
    if len(board) > row+1:
        if main == board[row+1][col] and main != ' ':
            
            board[row][col] = ' '
            board[row+1][col] = ' '
            row = row+1
            sayac = sayac+1
            return find_top(board, row, col,main),find_left(board, row, col,main),find_right(board, row, col,main),find_bottom(board, row, col,main,)

#sol komşu
def find_left(board, row, col, main):
    global sayac
    if  0 < col:
        if main == board[row][col-1] and main != ' ':
            main = board[row][col-1]
            board[row][col] = ' '
            board[row][col-1] = ' '
            col = col-1
            sayac = sayac+1
            return find_top(board, row, col,main),find_left(board, row, col,main),find_right(board, row, col,main),find_bottom(board, row, col,main,)

#sağ komşu
def find_right(board, row, col, main):
    global sayac
    if len(board[row]) > col+1:
        if main == board[row][col+1] and main != ' ':
            main = board[row][col+1]
            board[row][col] = ' '
            board[row][col+1] = ' '
            col = col+1
            sayac = sayac+1
            return find_top(board, row, col,main),find_left(board, row, col,main),find_right(board, row, col,main),find_bottom(board, row, col,main,)

#puan hesapla
def puan_hesapla(main):
    global puan
    puan = puan + (int(main) * int(fibonacci(sayac)))
    return puan

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Oyunu başlat
start_game()

#Oyun döngüsü
while end_game(kontrol(tablo)) == True:

    print_board(kontrol(tablo))
    row=int(input("Satır:"))-1
    col=int(input("Sütun:"))-1
    if row > len(tablo)-1 or col > len(tablo[0])-1:
        print("Düzgün bir büyüklük giriniz!")
        continue
    else:
        main=tablo[row][col]
    oyna(tablo,row,col,main)
    print("Puan: "+ str(puan_hesapla(main)))
    sayac = 1


print("Oyun Sona Ermiştir. Puanınız: "+str(puan))
dosyaya_yaz(eskiye_cevir(tablo))
    
    





