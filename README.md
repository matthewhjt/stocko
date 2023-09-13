# Tugas 2 - Stocko
<hr>

## Link menuju situs: https://stocko-pbp.adaptable.app/main/
- Nama: Matthew Hotmaraja Johan Turnip
- NPM: 2206081231
- Kelas: PBP C
<hr>

## Langkah-Langkah Mengimplementasi

### Setup Git dan Python Django
  1. Buat sebuah folder untuk projectnya
  2. Buat sebuah repository di GitHub
  3. Initialize repo git dengan
     ```
     git init
     ```
  4. Mengikut langkah-langkah dari GitHub/Tutorial (git add, commit, branch, remote add, dst)
  5. Membuat virtual environment Django dengan
     ```
     python -m venv env
     ```
  6. Masuk ke virtual environtment dengan
     ```
     env\Scripts\activate
     ```
     Note: Saya mengerjakan melalui VSCode, tidak perlu .bat
  7. Menyiapkan requirements.txt dan menginstallnya dengan
     ```
     pip install -r requirements.txt
     ``` 

### Membuat project Django dan konfigurasi settings.py
  8. Membuat project Django bernama "stocko" dengan:
     ```
     django-admin startproject stocko .
     ```
     Note: pakai . supaya projectnya dibuat di folder yang sama (jika tidak maka akan membuat folder baru di dalam folder sekarang)

  9. Membuka settings.py dan menambahkan "*" pada ALLOWED_HOSTS untuk mengizinkan semua host:
     ```
     ...
     ALLOWED_HOSTS = ["*"]
     ...
     ```
### Membuat aplikasi main
  10. Membuat sebuah app Django bernama 'main' dengan:
      ```
      python manage.py startapp main
      ```
  11. Mendaftarkan main pada INSTALLED_APPS di dalam settings.py:
      ```
      INSTALLED_APPS = [
      ...,
      'main',
      ...
      ]
      ```

### Melakukan routing
  12. Membuat urls.py pada direktori app main, lalu menambahkan:
      ```
      from django.urls import path
      from main.views import show_main

      app_name = 'main'

      urlpatterns = [
      path('', show_main, name='show_main'),
      ]
      ```
      Ini untuk mengonfigurasi routing pada app main. <br>
      import path default dari Django untuk mengatur path <br>
      show_main adalah sebuah function yang akan dibuat di views.py dalam app main <br>
      app_name berfungsi untuk nama url <br>
  13. Membuka urls.py pada direktori project untuk mengonfigurasi routing project dengan menambahkan:
      ```
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('main/', include('main.urls')),
      ]
      ```
      include digunakan untuk meng-include routing app main pada projectnya

### Membuat model untuk app main
  14. Pada direktori app main buka models.py lalu tambahkan:
      ```
      from django.db import models

      class Product(models.Model):
          name = models.CharField(max_length=255)
          amount = models.IntegerField()
          price = models.IntegerField()
          description = models.TextField()
      ```

      Class yang dibuat adalah class Product. Class tersebut memiliki atribut name, amount, price, description. name menggunakan CharField karena tidak         panjang. amount dan price menggunakan IntegerField karena akan menyimpan data berupa angka. Berbeda dengan name, description menggunakan TextField        karena bisa memiliki String yang panjang.

  15. Setelah itu, lakukan migrasi dengan:
      ```
      python manage.py makemigrations
      ```

      untuk membuat berkas migrasi, dan
      ```
      python manage.py migrate
      ```

      untuk melakukan migrasinya

      Note: setelah melakukan perubahan pada model harus dilakukan migrasi.

### Mengatur views.py dan templates
  16. Pertama-tama buat folder templates pada app main, lalu tambahkan main.html
      ```
      <h1>Stocko - Kelola Stock Toko</h1>
      <hr>
      <h3>Nama: {{nama}}</h3>
      <h3>NPM: {{npm}}</h3>
      <h3>Kelas: {{kelas}}</h3>
      ```
      untuk menampilkan nama, npm, dan kelas.
  17. Pada views.main dalam app main, tambahkan:
      ```
      from django.shortcuts import render

      def show_main(request):
          context = {
              'nama': 'Matthew Hotmaaja Johan Turnip',
              'npm' : '2206081231',
              'kelas': 'PBP C'
          }
  
      return render(request, "main.html", context)
      ```
      untuk membuat sebuah function yang akan menampilkan tampilan pada templates. request berguna untuk mengatur HTTPRequest, sementara itu context      berguna untuk menampung data-data yang akan ditampilkan (variable nama, npm, kelas). Render adalah sebuah function dari Django untuk merender/menampilkan tampilan templates.

### Deployment
  18. Terakhir, deploy app dengan menggunakan platform Adaptable.
<hr>

## Bagan Request Client
![image](https://github.com/matthewhjt/stocko/assets/112328487/da86070f-1937-4f04-8a04-08fdac1bced8)

## Mengapa Virtual Environment?
Kita menggunakan virtual environment untuk mengisolasi sistem development kita dari sistem pada komputer sehingga kita bisa mengelola proyek dengan baik. Hal ini dapat berguna ketika kita ingin melakukan kolaborasi. Misalnya, versi Python atau Django yang dipakai di virtual environment bisa sesuai dengan apa yang dikerjakan oleh tim tanpa harus bentrok dengan versi yang ada di komputer kita. Kita masih bisa membuat projek Django tanpa virtual environment tapi akan lebih baik menggunakannya untuk menghindari hal yang tidak diinginkan.

## MVC, MVT, MVVM
- MVC (Model-View-Controller)
  Pada tipe ini, model berfungsi untuk mengelola data, menghitung hasil, dan berkomunikasi dengan database. View berfungsi untuk menampilkan data kepada pengguna (seperti Template pada MVT/Django). Controller berfungsi untuk menghubungkan View dan Model, view menerima input, mengirimkannya pada model, menerima hasilnya lalu menampilkannya pada View.
  
- MVT (Model-View-Template)
  Tipe ini digunakan oleh Django. Mirip seperti MVC, Model juga berfungsi mengelola data, Template berfungsi menampilkan datanya (seperti View pada MVC), dan View menghubungkan Model dan Template (seperti Controller pada MVC).
  
- MVVM (Model-View-ViewModel)
  Pada tipe ini Model dan Viewnya sama seperti pada MVT. Bedanya, ada ViewModel yang memungkinkan pemisahan yang lebih jelas antara tampilan dan logika. 
  
      

      
      


     
