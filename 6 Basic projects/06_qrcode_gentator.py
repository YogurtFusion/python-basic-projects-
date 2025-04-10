import qrcode
# basic Generator
# img = qrcode.make('https://www.youtube.com/watch?v=yVl_G-F7m8c&t=295sw')
# type(img)
# img.save("1stqrcode.png")

# modified

data = input("Enter The Text or Url: "). strip()

file_name = input(f"Enter the filename: ").strip() 

# strip is for eleminating unnecessary space after text ends

qr = qrcode.QRCode(box_size=15, border=4)

qr.add_data(data)

image = qr.make_image(fill_color="white",back_color= "black" )

image.save(f"{file_name}.png")
print(f"your QR code saved as {file_name}")