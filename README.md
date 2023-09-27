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
- Akun Kedua

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
