#a very simple program that allows you to insert the data and the name of the photo of the qr code 
# and it generates the qr code

import qrcode

def create_qrcode(data, photo_name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data=data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(photo_name)
    print(f"QR Code saved as {photo_name}")

def ask_data():
    data=input("write your site link: ")
    photo_name=input("Enter the name you want to assign to the QR code photo, write also the file extension: ")
    return data, photo_name



def main():
   data, photo_name=ask_data()
   create_qrcode(data=data, photo_name=photo_name)



if __name__=="__main__":
    main()
