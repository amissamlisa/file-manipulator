import sys
import shutil

def reverse():
  input_path =  sys.argv[2]
  output_path =  sys.argv[3]
  reversed = ""
    
  try:
    s = open_file(input_path)
    reversed = s[::-1]
    write_file(output_path,reversed)
  except(FileNotFoundError):
    print("ファイルが見つかりません")

def copy():
  input_path =  sys.argv[2]
  output_path =  sys.argv[3]
    
  try:
    shutil.copy(input_path, output_path)
  except(FileNotFoundError):
    print("ファイルのパスが存在しません")

def duplicate_contents():
  input_path =  sys.argv[2]
  n = int(sys.argv[3])

  try:
    s = open_file(input_path)
    with open(input_path, mode='a') as f:
      f.write("\n")
      for i in range(n):
        f.write(s + "\n")
  except(FileNotFoundError):
    print("ファイルが見つかりません")    
  except(ValueError):
    print("数字を入力してください")

def replace_string():
  input_path = sys.argv[2]
  needle = sys.argv[3]
  new_string = sys.argv[4]

  try:
    s = open_file(input_path)
    s = s.replace(needle,new_string)
    write_file(input_path,s)
  except(FileNotFoundError):
    print("ファイルが見つかりません")    


def open_file(input_path):
  with open(input_path) as fi:
    s = fi.read()
    return s

def write_file(output_path,s):
    with open(output_path, 'w') as fo:
      fo.write(s)
    
if __name__ == "__main__":
  command = sys.argv[1]
  if command == "reverse":
    reverse()
  elif command == "copy":
    copy()
  elif command == "duplicate-contents":
    duplicate_contents()
  elif command == "replace-string":
    replace_string()