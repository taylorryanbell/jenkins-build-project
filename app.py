import os
import sys
import numpy

if len(sys.argv) != 2:
    print("incorrect argument amount")
    exit(1)

file_path = sys.argv[1]

if os.path.exists(file_path):
  os.remove(file_path)

file = open(file_path, "x")
file.write(f"""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lobster+Two&display=swap" rel="stylesheet">
</head>

<body style="overflow: hidden; background-color: ghostwhite;">
  <div style="height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center">
    <div style="font-family: 'Lobster Two'; font-size: 15rem;">PI: {numpy.pi}</div>
  </div>
</body>

</html>
""")
file.close()
