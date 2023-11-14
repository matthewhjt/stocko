# Stocko

<hr>

## Link menuju situs: http://matthew-hotmaraja-tugas.pbp.cs.ui.ac.id/

- Nama: Matthew Hotmaraja Johan Turnip
- NPM: 2206081231
- Kelas: PBP C

<br>

# Tugas 2

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

9. Membuka settings.py dan menambahkan "\*" pada ALLOWED_HOSTS untuk mengizinkan semua host:
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

    Class yang dibuat adalah class Product. Class tersebut memiliki atribut name, amount, price, description. name menggunakan CharField karena tidak panjang. amount dan price menggunakan IntegerField karena akan menyimpan data berupa angka. Berbeda dengan name, description menggunakan TextField karena bisa memiliki String yang panjang.

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

    untuk membuat sebuah function yang akan menampilkan tampilan pada templates. request berguna untuk mengatur HTTPRequest, sementara itu context berguna untuk menampung data-data yang akan ditampilkan (variable nama, npm, kelas). Render adalah sebuah function dari Django untuk merender/menampilkan tampilan templates.

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
<br>
<br>
<hr>

# Tugas 3

## Perbedaan POST <i>request</i> dan GET <i>request</i>

- GET
  <br>
  GET <i>request</i> digunakan untuk membaca atau menerima data dari sebuah <i>web server</i>. Jika berhasil menerima data, GET me<i>-return HTTP response status code</i> 200. Data <i>request</i> pada GET biasanya berupa <i>id</i> atau <i>data field lain</i> yang merujuk pada data yang diinginkan.

- POST
  <br>
  POST request digunakan untuk mengirimkan data berupa <i>file, form data</i>, dll. POST akan me<i>-return HTTP response status code</i> 201. Data yang dikirimkan akan mengubah data pada server atau membuat data baru pada server.

  Baik GET <i>request</i> maupun POST <i>request</i> bisa memiliki data atau tidak. Bedanya, data pada GET digunakan untuk memilih data yang ingin diambil dari <i>web/server</i>, sedangkan data pada POST digunakan untuk membuat data baru atau mengubah data yang ada.

## Perbedaan antara XML, JSON, dan HTML dalam konteks pengiriman data

- XML
  <br>
  XML harus memiliki <i>root element</i> dan harus memiliki <i>closing tag</i>. XML lebih deskriptif sehingga lebih mudah dibaca oleh manusia, terutama oleh masyarakat awam atau non-<i>programmer</i>. XML Document Object Model (DOM) memiliki struktur <i>tree</i> yang disebut <i>node-tree</i>. Pada XML DOM, teks dalam sebuah node bukan <i>value</i> dari node tersebut, tetapi adalah sebuah <i>text node</i>.
- JSON
  <br>
  JSON lebih ringkas dan lebih mudah dibaca oleh mesin, tetapi kurang deskriptif sehingga lebih sulit dibaca oleh manusia. Format JSON adalah berupa text. Data JSON mudah dibaca atau dibuat di banyak bahasa pemrograman sehingga banyak digunakan oleh <i>programmer</i>. JSON menyimpan data dalam bentuk <i>key and value</i> dan dipisah oleh tanda koma. Untuk menyimpan objek digunakan tanda kurung kurawal dan untuk menyimpan list/array digunakan tanda kurung siku.
- HTML
  <br>
  HTML adalah sebuah bahasa <i>markup</i> yang digunakan untuk menampilkan data atau konten <i>web</i>. HTML tidak digunakan untuk mengirimkan data, tapi untuk menampilkan data. HTML akan dirender oleh browser sehingga bisa ditampilkan kepada pengguna.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON lebih sering digunakan dalam pertukaran data karena format JSON lebih mudah untuk dibaca dan di<i>generate</i> oleh mesin. JSON lebih cepat dan lebih mudah untuk diproses dibandingkan XML. Selain itu, JSON tidak eksklusif digunakan dalam bahasa pemrograman Javascript, tetapi juga tersedia pada banyak bahasa lain. Oleh karena itu, JSON lebih sering digunakan pertukaran data.

## Langkah-Langkah Implementasi

### Mengatur routing dan mengimplementasi skeleton sebagai kerangka views

1.  Pada urls.py di directory stocko, ubah pathnya.

    ```
    urlpatterns = [
       path('', include('main.urls')),
       path('admin/', admin.site.urls),
    ]
    ```

2.  Pada root folder, buat folder template dan tambahkan base.html

    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            <title>Stocko - Tugas PBP</title>
            <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/5164/5164023.png" type="image/x-icon">
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>

    </html>
    ```

3.  Tambahkan BASE_DIR / 'templates pada settings.py

    ```
    TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
          'APP_DIRS': True,
          ...
      }
    ]
    ```

4.  Ubah main.html pada direktori main menjadi seperti berikut.

    ```
    {% extends 'base.html' %}

    {% block content %}
        <h1>Shopping List Page</h1>

        <h5>Name:</h5>
        <p>{{name}}</p>

        <h5>NPM: </h5>
        <p>{{npm}}</p>

        <h5>Class:</h5>
        <p>{{kelas}}</p>

    {% endblock content %}
    ```

### Membuat Input Form

1. Untuk membuat form, buat file forms.py pada folder main.

   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "amount", "price", "description"]
   ```

   Model berguna untuk menunjukkan model yang akan digunakan. Fields berguna untuk menunjukkan field dari model tersebut.

2. Pada views.py di main, tambahkan beberapa impor baru:

   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
   ```

3. Tambahkan funciton baru pada views.py yang berfungsi untuk melakukan penambahan produk.

   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse

   def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))

       context = {'form': form}
       return render(request, "create_product.html", context)

   ```

   POST <i>request</i> akan diassign ke variable form. Jika valid, form akan disimpan dan fungsi akan me<i>redirect</i> data form dengan return HTTPResponseRedirect.

4. Ubah function <i>show_main</i> sehingga menampilkan barang-barang yang sudah ditambahkan melalui <i>create_product</i>.

   ```
   def show_main(request):
   products = Product.objects.all()

   context = {
       'name': 'Matthew Hotmaraja Johan Turnip',
       'npm': '2206081231,
       'kelas': 'PBP C',
       'products': products
   }

   return render(request, "main.html", context)
   ```

   Product.objects.all() akan memanggil semua objek product yang sudah dibuat dari models.py. Setelah itu, objek tersebut dimasukkan ke dalam context untuk dirender oleh template.

5. Pada urls.py, impor fungsi <i>create_product</i>.
   ```
   from main.views import show_main, create_product
   ```
6. Tambahkan path untuk create_product.
   ```
   ...
   path('create-product', create_product, name='create_product'),
   ...
   ```
7. Buat <i>create_product.html</i> pada main/templates.

   ```
   {% extends 'base.html' %}

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>

   {% endblock %}
   ```

   <i> form method="POST"</i> menandakan bahwa form tersebut memiliki method POST. <i>csrf_token</i> adalah token yang dibuat Django untuk security. <i>form.as_table</i> berarti form akan disajikan berupa table.

8. Menambahkan tabel produk dan button untuk menambah produk ke dalam main.html.

   ```
   <table>
      <tr>
          <th colspan="4">Anda menyimpan {{products.count}} produk pada aplikasi Stocko</th>
      </tr>
     <tr>
         <th>Name</th>
         <th>Price</th>
         <th>Description</th>
         <th>Date Added</th>
     </tr>

     {% for product in products %}
         <tr>
             <td>{{product.name}}</td>
             <td>{{product.amount}}</td>
             <td>{{product.price}}</td>
             <td>{{product.description}}</td>
         </tr>
     {% endfor %}
   </table>

   <br>

   <a href="{% url 'main:create_product' %}">
       <button>
           Add New Product
       </button>
   </a>
   ```

### Membuat fungsi baru untuk melihat objek dalam bentuk HTML, XML, JSON, XML by id, dan JSON by id

1. Pada views.py, tambahkan beberapa impor baru.

   ```
   from django.http import HttpResponse
   from django.core import serializers
   ```

   Serializers berfungsi untuk mentranslate data menjadi bentuk XML atau JSON sesuai argument yang diberikan.

2. Pada views.py dalam main, buat fungsi baru untuk menunjukkan data dalam bentuk XML dan JSON

   ```
   def show_xml(request):
     data = Product.objects.all()
     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

   Untuk xml by id dan JSON by id, data atau produk difilter sesuai idnya dengan menambahkan <i>.filter(pk=id)</i>

3. Setelah itu, tambahkan fungsi-fungsi tersebut dengan menambahkan import pada urls.py
   ```
   from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id
   ```
4. Lalu, tambahkan path baru untuk fungsi-fungsi tersebut.
   ```
   path('xml/', show_xml, name='show_xml'),
   path('json/', show_json, name='show_json'),
   path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ```
5. Untuk membuat fungsi <i>show_html</i>, buat fungsi baru yang hanya akan menampilkan objek dalam HTML.

   ```
   def show_html(request):
   data = Product.objects.all()

   context = {
       'products': data,
   }

   return render(request, "show_product.html", context)
   ```

   Fungsi ini mirip dengan show_main, tetapi hanya akan menampilkan produk saja.

6. Setelah itu, buat <i>show_product.html</i> pada main/templates.

   ```
   {% extends 'base.html' %}

   {% block content %}
   <table>
       <tr>
           <th colspan="4">Anda menyimpan {{products.count}} produk pada aplikasi Stocko</th>
       </tr>
       <tr>
           <th>Name</th>
           <th>Amount</th>
           <th>Price</th>
           <th>Description</th>
       </tr>

       {% for product in products %}
           <tr>
               <td>{{product.name}}</td>
               <td>{{product.amount}}</td>
               <td>{{product.price}}</td>
               <td>{{product.description}}</td>
           </tr>
       {% endfor %}
   </table>
   {% endblock content %}
   ```

   Isinya sama seperti apa yang ditambahkan pada main.html, tetapi sekarang tanpa nama, npm, dan kelas.

7. Sama seperti function lainnya, tambahkan fungsi pada import dalam urls.py

   ```
   from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id, show_product
   ```

8. Tambahkan juga path baru pada urls.py
   ```
   path('html/', show_html, name='show_html')
   ```

## Screenshot Postman

- localhost:8000/xml
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/e4857bec-02f4-4a7a-ab17-0a76ba386518)

- localhost:8000/json
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/7c9bfed8-69d8-4ffe-b481-d085b115d71e)

- localhost:8000/xml/1
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/7c72e393-2a4e-45a4-b1e0-3a3ba734ba60)

- localhost:8000/json/1
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/195a5e4f-3a2a-4248-a65b-3ddf741bd7af)

- localhost:8000/html
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/4ccf1c77-0f34-497b-8394-47d704847188)
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/6036e247-9822-4f8c-80f9-7988554431fc)

<br>
<hr>

# Tugas 4

## Django UserCreationForm

Django UserCreationForm adalah formulir pendaftaran bawaan Django. Dengan UserCreationForm, programmer tidak perlu membuat fitur pendaftaran pada aplikasi web dari awal karena sudah tersedia.

Beberapa kelebihan menggunakan Django UserCreationForm:

- UserCreationForm memudahkan programmer untuk mengembangkan fitur pendaftaran tanpa harus menulis kode dari awal.
- UserCreationForm sudah terintegrasi dengan project atau app Django sehingga bisa dihubungkan dengan komponen Django lainnya dengan mudah.

Sementara itu, beberapa kekurangan Django UserCreationForm:

- Tampilannya sederhana sehingga kurang bagus dilihat. Jika ingin melakukan kustomisasi penampilan perlu menggunakan HTML dan CSS tambahan.
- Fiturnya terbatas sehingga mungkin tidak cocok untuk aplikasi tertentu.

## Perbedaan Autentikasi dan Otorisasi dalam Django

Authentication adalah proses identifikasi seseorang atau sebuah aplikasi saat ingin memasuki sebuah sistem (login). Authentication bertujuan untuk memastikan (memverifikasi) seseorang atau sebuah aplikasi yang masuk memang boleh masuk ke dalam sistem dan berinteraksi dengan sistem.

Authorization adalah proses verifikasi fitur-fitur apa saja yang dapat diakses oleh pengguna yang telah terautentikasi. Proses ini memastikan pengguna hanya dapat mengakses fitur-fitur sistem yang sesuai dengan peran (role) pengguna tersebut.

Kedua hal tersebut merupakan hal yang penting dalam pengembangan aplikasi karena kedua hal tersebut dapat menjaga keamanan sistem dari peretas. Jika tidak ada autentikasi dan otorisasi, semua orang atau sistem lain dapat memasuki sistem aplikasi secara bebas dan bahkan merusak sistem tersebut.

## Cookies Dalam Aplikasi Web dan Penggunaannya oleh Django

Cookies adalah data kecil yang disimpan di sisi <i>client</i> (<i>browser</i>) saat pengguna berinteraksi dan menggunakan sistem aplikasi. Cookies menyimpan informasi tentang pengguna untuk mengidentifikasi pengguna. Django menggunakan cookies untuk mengelola data sesi pengguna. Data sesi adalah cara untuk menyimpan informasi spesifik pengguna antara permintaan HTTP yang berbeda sehingga pengguna dapat mengakses halaman/fitur lain dari sistem tanpa harus melakukan login kembali. Dengan menggunakan cookies dan data sesi, Django dapat melacak informasi pengguna selama sesi mereka di situs web Anda tanpa harus mengandalkan parameter URL atau menyimpan semua data di sisi server.

## Keamanan Cookies Secara <i>Default</i> Dalam Pengembangan Web

Penggunaan <i>cookies</i> secara <i>default</i> (tanpa modifikasi atau validasi tambahan) dalam pengembangan aplikasi <i>web</i> tidak aman. Hal ini karena terdapat beberapa resiko keamanan sistem. Salah satu contohnya adalah <i>cookies poisoning</i>, di mana penyerang atau peretas memodifikasi <i>cookies</i> untuk memperoleh akses <i>unauthorized</i>. Selain itu, <i>cookies</i> rentan terhadap pencurian dan dapat dimanfaatkan untuk mendapatkan akses ke dalam sistem aplikasi.

## Cara Mengimplementasi Tugas 4

### Membuat fungsi registrasi

1. Pada main.views lakukan beberapa import.

   - messages untuk notifikasi sukses/gagal/peringatan.

   ```
   from django.contrib import messages
   ```

   - datetime untuk informasi cookies pengguna

   ```
   import datetime
   ```

   - UserCreationForm untuk fungsi registrasi

   ```
   from django.contrib.auth.forms import UserCreationForm
   ```

   - authenticate dan login untuk fungsi login, dan logout untuk fungsi logout

   ```
   from django.contrib.auth import authenticate, login, logout
   ```

2. Tambahkan function baru untuk melakukan registrasi pada sistem.

   - Fungsi register untuk registrasi

     ```
     def register(request):
         form = UserCreationForm()

         if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 messages.success(request, 'Your account has been successfully created!')
                 return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
     ```

     Fungsi tersebut akan menyimpan form registrasi lalu meredirect pengguna ke halaman login.

   - Fungsi login_user untuk login

     ```
     def login_user(request):
         if request.method == 'POST':
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request, username=username, password=password)
             if user is not None:
                 if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
             else:
                 messages.info(request, 'Sorry, incorrect username or password. Please try again.')
         context = {}
         return render(request, 'login.html', context)
     ```

     Fungsi tersebut akan mengambil username dan password dari data POST request, lalu mengautentikasinya. Akan ada messages gagal login jika username atau password yang dimasukkan salah.

   - Fungsi logout_user untuk logout

     ```
     def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
     ```

3. Buat file HTML di dalam main/templates untuk halaman registrasi dan login, dan menambahkan button logout pada main.html.

   - register.html untuk halaman registrasi

     ```
     {% extends 'base.html' %}

     {% block meta %}
         <title>Register</title>
     {% endblock meta %}

     {% block content %}

     <div class = "login">

         <h1>Register</h1>

             <form method="POST" >
                 {% csrf_token %}
                 <table>
                     {{ form.as_table }}
                     <tr>
                         <td></td>
                         <td><input type="submit" name="submit" value="Daftar"/></td>
                     </tr>
                 </table>
             </form>

         {% if messages %}
             <ul>
                 {% for message in messages %}
                     <li>{{ message }}</li>
                     {% endfor %}
             </ul>
         {% endif %}

     </div>

     {% endblock content %}
     ```

     File HTML tersebut akan menampilkan formulir registrasi dalam bentuk table ( {{ form.as_table }} ).

   - login.html untuk halaman login

     ```
        {% extends 'base.html' %}

        {% block meta %}

        <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>

                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}

            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}

     ```

     File HTML tersebut akan menampilkan form login sebagai table dan link ke halaman register jika pengguna belum memiliki akun.

   - Pada main.html tambah button Logout

     ```
     ...
     <a href="{% url 'main:logout' %}">
         <button>
             Logout
         </button>
     </a>
     ...
     ```

4. Pada main.urls tambahkan function yang sudah dibuat dan tambahkan juga pathnya.

   ```

   from main.views import register, login_user, logout_user

   ```

   ```

   ...
   path('register/', register, name='register'),
   path('login/', login_user, name='login'),
   path('logout/', logout_user, name='logout'),
   ...

   ```

5. Menambahkan restriksi ke tiap fungsi yang perlu informasi user. Pada main.views import login_required.

   ```
   from django.contrib.auth.decorators import login_required

   ```

6. Tambahkan kode @login_required(login_url='/login') untuk setiap fungsi di views.py (kecuali fungsi register, login, logout)

### Membuat dua akun dengan data dummy di lokal

- Akun Pertama
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/c9634761-7ca1-4da5-8627-6e25f09927b0)

- Akun Kedua
  ![image](https://github.com/matthewhjt/stocko/assets/112328487/1c77a477-aaf9-4564-a94f-9e48827d9aa4)

### Menghubungkan model Product dan User

1. Pada main.models import User

   ```
   from django.contrib.auth.models import User
   ```

2. Modifikasi class Product dengan menambah field user

   ```
   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       ...
   ```

   ForeinKey berfungsi menambahkan relationship/hubungan terhadap User dari objek produk tersebut. Ketika User dihapus, maka objek produk milik User tersebut juga akan terhapus (cascade)

3. Modifikasi views.create_product untuk mengatur user dari objek yang dibuat.

   ```
   def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
           product = form.save(commit=False)
           product.user = request.user
           product.save()
           return HttpResponseRedirect(reverse('main:show_main'))
       ...
   ```

   commit=False berguna agar objek tidak langsung disimpan di database, tetapi usernya di-set dahulu sesuai request.

4. Modifikasi setiap fungsi supaya memfilter berdasarkan akun.

   Untuk setiap fungsi yang akan menampilkan data (show xml, json, xml by id, json by id, html), ubah data agar product difilter sesuai usernya.

   ```
   data = Product.objects.filter(user=request.user)
   ```

### Menampilkan informasi username dan last login

1. Modifikasi fungsi show_main menjadi

   ```
   def show_main(request):
       products = Product.objects.filter(user=request.user)

       context = {
           'name': request.user.username,
           'last_login': request.COOKIES['last_login'],
       ...
   ...
   ```

   'name' dalam konteks akan berubah sesuai request, last login akan menampilkan data cookies last login.

2. Tambahkan kode html berikut setelah tabel data dan sebelum button Add New Product dan Logout.

   ```
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```

# Tugas 5

## Manfaat Element Selector

- Universal Selector
  Universal selector berfungsi untuk memilih semua elemen di dalam dokumen HTML. Universal selector digunakan ketika kita ingin mengubah keseluruhan dokumen. Jarang digunakan

- Element Selector
  Element selector berfungsi untuk memilih semua elemen yang memiliki tag HTML yang sama di dalam dokumen HTML. Element selector digunakan saat kita ingin mengubah element dalam HTML sesuai tagnya.

- ID Selector
  ID selector berfungsi untuk memilih elemen berdasarkan tagnya. ID Selector digunakan ketika kita ingin mengubah elemen spesifik karena id bersifat unik.

- Class Selector
  Class selector berfungsi untuk mengelompokkan elemen dengan karakteristik yang sama. Class selector digunakan ketika kita ingin memodifikasi sebuah kelompok tag/class tertentu di dalam dokumen HTML

## Tag HTML5

- Header
  Header adalah tag HTML yang menandakan bahwa elemen-elemen di dalam tag tersebut adalah kepala dari dokumen (contohnya untuk menampung navbar)

- Nav
  Nav digunakan untuk mengelompokkan elemen yang berfungsi sebagai navigasi dalam suatu website

- Main
  Main adalah tag utama di HTML, isinya adalah elemen-elemen utama yang ditampilkan pada sebuah halaman website

- Form
  Form adalah tag HTML untuk menerima formulir input dari pengguna

- Input
  Input biasanya digunakan bersamaan dengan form untuk menampung data input.

- Textarea
  Textarea adalah salah satu jenis input untuk menampung teks yang panjang

## Perbedaan Margin dan Padding

Margin adalah ruang di luar elemen (di sekitar border) yang mengosongkan area di sekitar border. Sementara itu, Padding adalah ruang di dalam elemen yang mengosongkan area di sekitar konten. Keduanya tidak terlihat alias transparan

## Perbedaan Framework Tailwind dan Bootstrap

- Tailwind

  - Tailwind CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.
  - Tailwind CSS memiliki file CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada

- Bootstrap

  - Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.

  - Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.

# Implementasi

1.  Menginstal Bootstrap
2.  Menambahkan header navbar pada main.html dan create_product.html

        <header>
        <nav class="navbar navbar-dark bg-dark">
            <div class="container-fluid d-flex justify-content-center text-white text-center">
                <h5>{{nama}} <br><br> {{kelas}}</h5>
            </div>
        </nav>

        <nav class="navbar navbar-expand-xl navbar-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="{% url 'main:show_main' %}">
                    <img src="https://cdn-icons-png.flaticon.com/512/5164/5164023.png" width="30" height="30" alt=""> Stocko
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <a class="nav-link active" aria-current="page" href="{% url 'main:create_product' %}">Add New Product</a>
                    </div>
                    <div class="text-white">
                        <a href="{% url 'main:logout' %}">
                            <button type="button" class="btn btn-danger">Logout</button>
                        </a>
                    </div>
            </div>
        </nav>

        </header>

3.  Mengubah tampilan halaman main, register, login, dan create_product

    - login.html

      ```
      {% extends 'base.html' %}

      {% block meta %}
          <title>Login</title>
      {% endblock meta %}

      {% block content %}

      <div class="container-fluid p-2 h-100 d-flex flex-column align-items-center bg-dark text-white">

          <div class = "login p-2 d-flex flex-column align-items-center">

              <h1>Login</h1>
              <br>
              <form method="POST">
                  {% csrf_token %}
                  <div class="form-group">
                      <label for="id_username">Username</label>
                      <input type="text" name="username" class="form-control" placeholder="Username">
                  </div>
                  <br>
                  <div class="form-group">
                      <label for="id_password">Password</label>
                      <input type="password" name="password" class="form-control" placeholder="Password">
                  </div>
                  <br>
                  <div class="text-center">
                      <button type="submit" class="btn btn-primary">Login</button>
                  </div>
              </form>

              {% if messages %}
                  <ul>
                      {% for message in messages %}
                          <li>{{ message }}</li>
                      {% endfor %}
                  </ul>
              {% endif %}

              <br>
              Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

          </div>

      </div>

      {% endblock content %}
      ```

    - register.html

      ```
      {% extends 'base.html' %}

        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}

        <div class="container-fluid p-2 h-100 d-flex flex-column align-items-center bg-dark text-white">

            <div class = "login p-2 d-flex flex-column align-items-center">

                <h1>Register</h1>

                    <form method="POST" >
                        {% csrf_token %}
                        <div class="form-group">
                            <label for="id_username">Username*</label>
                            <input type="text" name="username" class="form-control" maxlength="150" autocapitalize="none" autocomplete="username" autofocus required id="id_username">
                            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
                        </div>
                        <br>
                        <div class="form-group">
                            <label for="id_password1">Password*</label>
                            <input type="password" name="password1" class="form-control" autocomplete="new-password" required id="id_password1">
                            <ul>
                                <li>Your password can’t be too similar to your other personal information.</li>
                                <li>Your password must contain at least 8 characters.</li>
                                <li>Your password can’t be a commonly used password.</li>
                                <li>Your password can’t be entirely numeric.</li>
                            </ul>
                        </div>
                        <br>
                        <div class="form-group">
                            <label for="id_password2">Password Confirmation*</label>
                            <input type="password" name="password2" class="form-control" autocomplete="new-password" required id="id_password2">
                            Enter the same password as before, for verification.
                        </div>
                        <br>
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary">Register</button>
                        </div>
                    </form>

                    <br>
                    Already have an account? <a href="{% url 'main:login' %}">Login</a>

                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}

            </div>

        </div>

        {% endblock content %}
      ```

    - create_product.html

      ```
      {% extends 'base.html' %}

      {% block content %}

      <header>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-fluid d-flex justify-content-center text-white text-center">
                  <h5>{{nama}} <br><br> {{kelas}}</h5>
              </div>
          </nav>
          <nav class="navbar navbar-expand-xl navbar-dark">

              <div class="container-fluid">
              <a class="navbar-brand" href="{% url 'main:show_main' %}">
                  <img src="https://cdn-icons-png.flaticon.com/512/5164/5164023.png" width="30" height="30" alt=""> Stocko
              </a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                  <div class="navbar-nav">
                  <a class="nav-link active" aria-current="page" href="{% url 'main:create_product' %}">Add New Product</a>
                  </div>
                  <div class="text-white">
                      <a href="{% url 'main:logout' %}">
                          <button type="button" class="btn btn-danger">Logout</button>
                      </a>
                  </div>
              </div>
              </div>
          </nav>
      </header>
      <div class="container-fluid text-white">
      <h1>Add New Product</h1>
          <form method="POST" class="col-md-3">
              {% csrf_token %}
              <div class="form-group">
                  <label for="name">Name: </label>
                  <input type="text" name="name" class="form-control" required id="id_name" placeholder="Name">
              </div>
              <br>
              <div class="form-group">
                  <label for="amount">Amount: </label>
                  <input type="number" name="amount"  class="form-control" required id="id_amount" placeholder="1">
              </div>
              <br>
              <div class="form-group">
                  <label for="price">Price: </label>
                  <input type="number" name="price"  class="form-control" required id="id_price" placeholder="1">
              </div>
              <br>
              <div class="form-group">
                  <label for="description">Description: </label>
                  <textarea name="description" class="form-control" cols="40" rows="10" required id="id_description"></textarea>
              </div>
              <br>
              <div class="container">
                  <button type="submit" class="btn btn-primary">Add Product</button>
              </div>
          </form>
      </div>

      {% endblock %}
      ```

    - main.html

      ```
      {% extends 'base.html' %}

      {% block content %}
      <header>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-fluid d-flex justify-content-center text-white text-center">
                  <h5>{{nama}} <br><br> {{kelas}}</h5>
              </div>
          </nav>
          <nav class="navbar navbar-expand-xl navbar-dark">

              <div class="container-fluid">
                  <a class="navbar-brand" href="{% url 'main:show_main' %}">
                  <img src="https://cdn-icons-png.flaticon.com/512/5164/5164023.png" width="30" height="30" alt=""> Stocko
                  </a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                  <div class="navbar-nav">
                      <a class="nav-link active" aria-current="page" href="{% url 'main:create_product' %}">Add New Product</a>
                  </div>
                  <div class="text-white">
                      <a href="{% url 'main:logout' %}">
                          <button type="button" class="btn btn-danger">Logout</button>
                      </a>
                  </div>
                  </div>
              </div>
              </nav>
      </header>

      <div class="container-fluid bg-dark text-white p-2 table-responsive">
          <table class="table table-striped table-dark table-bordered table-hover table-fixed">
              <thead class="thead-dark">
                  <tr>
                      <th class="text-center" colspan="7">Anda menyimpan {{products.count}} produk pada aplikasi ini</th>
                  </tr>
                  <tr>
                      <th class="th-sm text-center">Name</th>
                      <th class="th-sm text-center">Amount</th>
                      <th class="th-sm text-center">Price</th>
                      <th class="w-75 text-wrap" style="width: 6rem;">Description</th>
                  </tr>
              </thead>

              {% for product in products %}
                  <tr {% if forloop.last %} class = "table-danger" {% endif %}>
                      <td>{{product.name}}</td>
                      <td class="text-center">{{product.amount}}</td>
                      <td class="text-center">{{product.price}}</td>
                      <td>{{product.description}}</td>
                      <td class="text-center">
                          <a href="{% url 'main:add_amount' id=product.id %}">
                              <button class="btn btn-primary">
                                  Add
                              </button>
                          </a>
                      </td>
                      <td class="text-center">
                          <a href="{% url 'main:subtract_amount' id=product.id %}">
                              <button class="btn btn-primary">
                                  Subtract
                              </button>
                          </a>
                      </td>
                      <td class="text-center">
                          <a href="{% url 'main:delete_product' id=product.id %}">
                              <button class="btn btn-danger">
                                  Delete
                              </button>
                          </a>
                      </td>
                  </tr>
              {% endfor %}
          </table>

          <br />

          <h5>Sesi terakhir login: {{ last_login }}</h5>

      </div>
      {% endblock content %}
      ```

# Tugas 6

## Perbedaan <i>asynchronous programming</i> dan <i>synchronous programming</i>

Pada <i>synchronous programming</i>, program dieksekusi secara berurutan dan satu per satu. Pengguna harus menunggu program lalu me-<i>refresh</i> halaman baru untuk melanjutkan menggunakan <i>website</i>. Sementara itu, pada <i>asynchronous programming</i>, program dapat dieksekusi secara bersamaan atau secara paralel dengan program lainnya. Pengguna bisa menggunakan <i>website</i> tanpa harus menunggu tampilan halaman baru.

## Paradigma <i>Event-Driven Programming</i> dan Contoh

<i>Event-Driven Programming</i> merupakan salah satu paradigma yang didasarkan pada peristiwa (<i>event</i>) yang terjadi pada program. <i>Event</i> yang dimaksud dapat berupa input dari pengguna seperti <i>input form</i> atau saat pengguna mengklik sebuah <i>button</i>. Program akan bereaksi terhadap input yang diberikan oleh pengguna (<i>event handling</i>). Contohnya pada tugas PBP adalah <i>button</i> Add New Product dan Delete Product yang akan bereaksi ketika pengguna mengklik <i>button</i> tersebut.

## Penerapan <i>asynchronous programming</i> pada AJAX.

Asynchronous JavaScript and XML (AJAX) adalah salah satu teknik baru untuk menciptakan sebuah aplikasi web yang lebih bagus dan lebih interaktif. Dengan AJAX, <i>asynchronous programming</i> dapat diterapkan pada aplikasi web sehingga aplikasi web dapat diperbarui tanpa harus membuat penggunanya menunggu (menghindari pengguna harus me-<i>refresh</i> halaman setiap ada perubahan).

## Perbandingan Fetch API dan JQuery

Penerapan AJAX dapat dilakukan dengan menggunakan Fetch API maupun JQuery. Baik Fetch API dan jQuery adalah dua cara yang umum digunakan untuk menerapkan AJAX dalam pengembangan web. Namun, kedua teknologi ini memiliki karakteristik dan kelebihan yang berbeda.

JQuery adalah sebuah library JavaScript yang memiliki fitur AJAX built-in. JQuery mudah digunakan untuk AJAX dan memiliki kompabilitas dengan <i>browser</i> lama. Di sisi lain, Fetch API adalah sebuah alternatif yang merupakan bagian dari standar JavaScript modern. Fetch API terintegrasi dengan promise yang memudahkan penanganan respons dan penanganan kesalahan. Fetch API lebih ringan daripada jQuery karena tidak memerlukan unduhan library tambahan. Menurut saya, Fetch API lebih baik digunakan daripada JQuery karena Fetch API merupakan standar website modern. Selain itu, Fetch API mendapat dukungan dari komunitas JavaScript yang besar. Fetch API juga menyediakan promise sehingga dapat menangani response dan error dengan lebih baik.

## Implementasi Tugas

### Menampilkan Data pada halaman main

1. Membuat function yang akan mengambil (get) objek Product dalam bentuk json

   ```
   @login_required(login_url='/login')
    def get_product_json(request):
        product_item = Product.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', product_item))
   ```

2. Menambahkan path untuk function pada urls.py

   ```
   path('get-product/', get_product_json, name='get_product_json'),
   ```

3. Mengubah main.html sehingga product ditampilkan menggunakan function AJAX

   ```
   <div id="product_cards">

   </div>
   ```

4. Menambahkan block <i>script</i> dan fuction yang akan menampilkan produk.

   ```
   <script>
   async function getProducts() {
       return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
   }

   async function refreshProducts() {

       const products = await getProducts()
       let htmlString = '<div class="p-2 row row-cols-1 row-cols-md-4">'
       products.forEach((product) => {

           htmlString +=
               `\n\t<div class="p-3 card-row col mb-4">`

           if (product == products[products.length - 1]){
               htmlString +=
               `\n\t<div class="p-2 card mb-3 bg-danger bg-gradient text-white shadow rounded">`
           } else {
               htmlString +=
               `\n\t<div class="p-2 card mb-3 bg-secondary bg-gradient text-white shadow rounded">`
           }

           htmlString +=
                       `<div class="card-header">
                           <img src="https://cdn-icons-png.flaticon.com/512/5164/5164023.png" width="250" height="250" alt="" class="card-img-top">
                       </div>
                       <div class="card-body">
                           <h5 class="card-title">${product.fields.name}</h5>
                           <h6 class="card-subtitle mb-2">Amount: ${product.fields.amount}</h6>
                           <h6 class="card-subtitle mb-2">Price: ${product.fields.price}</h6>
                           <p class="card-text text">${product.fields.description}</p>
                           <div class="text-center">
                               <button type="button" class="btn btn-primary border-dark shadow rounded" onclick=addAmount(${product.pk})>Add</button>
                               <button type="button" class="btn btn-primary border-dark shadow rounded" onclick=subtractAmount(${product.pk})>Subtract</button>
                               <button type="button" class="btn btn-danger border-dark shadow rounded" onclick=deleteProduct(${product.pk})>Delete</button>
                           </div>
                       </div>
                   </div>
               </div>`
       })
       htmlString += '\n</div>'

       document.getElementById("product_cards").innerHTML = htmlString
   }

   refreshProducts()
   </script>
   ```

   Pertama-tama, semua objek Product akan diambil dengan function getProduct, lalu function refreshProduct akan menampilkan objek tersebut dalam bentuk Cards

### Menambahkan function untuk menambah produk secara AJAX

1. Membuat modal yang akan menerima input form dan button yang akan membuka modal tersebut.

   ```
   <div class="text-center">
       <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
   </div>

   <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
       <div class="modal-dialog">
           <div class="modal-content bg-dark">
               <div class="modal-header">
                   <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                   <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
               </div>
               <div class="modal-body">
                   <form id="form" onsubmit="return false;">
                       {% csrf_token %}
                       <div class="mb-3">
                           <label for="name" class="col-form-label">Name:</label>
                           <input type="text" class="form-control" id="name" name="name"></input>
                       </div>
                       <div class="mb-3">
                           <label for="amount" class="col-form-label">Amount:</label>
                           <input type="number" class="form-control" id="amount" name="amount"></input>
                       </div>
                       <div class="mb-3">
                           <label for="price" class="col-form-label">Price:</label>
                           <input type="number" class="form-control" id="price" name="price"></input>
                       </div>
                       <div class="mb-3">
                           <label for="description" class="col-form-label">Description:</label>
                           <textarea class="form-control" id="description" name="description"></textarea>
                       </div>
                   </form>
               </div>
               <div class="modal-footer">
                   <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                   <button type="button" class="btn btn-primary" id="button_add_product" data-bs-dismiss="modal">Add Product</button>
               </div>
           </div>
       </div>
   </div>
   ```

2. Membuat fungsi yang akan menambah product secara AJAX pada views.py

   ```
   @login_required(login_url='/login')
   @csrf_exempt
   def add_product_ajax(request):
       if request.method == 'POST':
           name = request.POST.get("name")
           amount = request.POST.get("amount")
           price = request.POST.get("price")
           description = request.POST.get("description")
           user = request.user

           new_product = Product(name=name, amount=amount, price=price, description=description, user=user)
           new_product.save()

           return HttpResponse(b"CREATED", status=201)
       return HttpResponseNotFound()
   ```

   Sama seperti yang biasa, tetapi function akan mereturn HTTPResponse, bukan me-redirect user.

3. Menambahkan fungsi add product pada block script

   ```
   function addProduct() {
           fetch("{% url 'main:add_product_ajax' %}", {
               method: "POST",
               body: new FormData(document.querySelector('#form'))
           }).then(refreshProducts)

           document.getElementById("form").reset()
           return false
       }

       document.getElementById("button_add_product").onclick = addProduct
   ```

   Fungsi akan ditambahkan pada button add product sehingga ketika button tersebut diklik fungsi ini akan dipanggil

### Menambah function lain seperti Add Amount, Subtract Amount, dan Delete Product

1. Menambahkan fungsi add, subtract, dan delete secara AJAX pada views.py

   ```
   @login_required(login_url='/login')
   def add_amount_ajax(request, id):
       product = Product.objects.get(user=request.user, pk=id)
       product.add_amount()
       product.save()
       return HttpResponse(b"UPDATED", status=204)

   @login_required(login_url='/login')
   def subtract_amount_ajax(request, id):
       product = Product.objects.get(user=request.user, pk=id)
       product.subtract_amount()
       product.save()
       return HttpResponse(b"UPDATED", status=204)

   @login_required(login_url='/login')
   def delete_product_ajax(request, id):
       product = Product.objects.get(user=request.user, pk=id)
       product.delete()
       return HttpResponse(b"DELETED", status=204)
   ```

   Sama seperti Add New Product, fungsi-fungsi ini sudah dibuat di tugas sebelumnya, hanya saja dimodifikasi sehingga hanya mereturn HTTPResponse, bukan meredirect halaman.

2. Menambahkan fungsi pada block script html

   ```
   function addAmount(id) {
       fetch("add-amount-ajax/" + id).then(refreshProducts)
   }

   function subtractAmount(id) {
       fetch("subtract-amount-ajax/" + id).then(refreshProducts)
   }

   function deleteProduct(id) {
       fetch("delete-product-ajax/" + id).then(refreshProducts)
   }
   ```

   Setiap button pada cards masing-masing memiliki atribut onclick yang akan memanggil fungsi di atas ketika button tersebut diklik. Fungsi tersebut akan mem-<i>fetch</i> setiap url fungsi lalu me-<i>refresh</i> produk secara <i>asynchronous</i>.

### Melakukan Collecstatic

1. Import os ke settings.py

   ```
   import os
   ```

2. Menambahkan PROJECT_ROOT dan STATIC_ROOT pada settings.py

   ```
   PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
   STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
   ```

3. Pada terminal, lakukan perintah Collecstatic

   ```
   python manage.py collecstatic
   ```
