"# server_repairup" 
สำหรับ หลังบ้าน
------------------------------------------
virtualenv env

.\env\Scripts\activate สลับมาใช้ ไพธอนที่ env 

pip install -r requirements.txt

------------------------------------------

python manage.py makemigrations  สร้างไฟล์ที่จะเขียนฐานข้อมูล (ทำทุกครั้งที่มีการเปลี่ยนแปลงไฟล์ โมเดล)

python manage.py migrate  อัพเดทฐานข้อมูล --- ทำต่อจากขั้นตอนมะกี่ทุกครั้ง 

python manage.py createsuperuser  สร้างแอดมิน

python manage.py runserver  เปิดโปรเจคฝั่งหลังบ้าน

------------------------------------------
อัปเข้า git

git add .

git commit -m "Commit"

git push

------------------------------------------
อัปลงคอม

git pull

------------------------------------------
git clone ...      ...