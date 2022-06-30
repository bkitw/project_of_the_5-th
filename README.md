# PyBakers Mini Organizer

![logo](https://user-images.githubusercontent.com/96789294/176653028-83e9a866-bbc0-4384-a8b9-f87cf20fd64d.jpg)

*Здесь представлено видение троих студентов-энтузиастов программы, ориентированной на сохранение конкретных данных пользователем, а также их последующий вывод. Программа позволит сохранить имена контактов, их номера телефонов, адреса электронной почты и дату рождения. Также программа реализует возможность работы с заметкам, для записи важных мыслей и такого прочего. Вишенкой на торте является функция "наведения порядка в директории", так называемый "file-sorter", который обязательно засунет особенно нужный файл в особенно далёкое место, разбирая папку, которая вот уже два с половиной года пылится у вас на диске D.*
### Демо:
Взглянуть и кратко ознакомиться с деталями интерфейса можно на скриншотах ниже:


![Screenshot_1](https://user-images.githubusercontent.com/98377639/176487857-420b74b5-5f8e-407a-9f68-e499014923ea.png)


![Screenshot_2](https://user-images.githubusercontent.com/98377639/176487877-54d221ea-6420-47b7-acbc-9043789f499c.png)


У приложения и каждого из его аспектов масса особенностей, опробовать которые вы сможете, лишь установив -- их не отобразить снимком экрана.

### Технологии:
В процессе разработки были использованы технологии среды разработки PyCharm, сайт-организатор Trello, непосредственно сервис GitHub и ряд простейших библиотек, доступных языку разработки.

### Особенности:
Характерной чертой этого проекта является его оригинальность в каждом из модулей, который он представляет, так как в процессе разработки создатели получили максимальную свободу самовыражения и следовали единственно верному для новичка принципу -- делай, чтобы работало, но делай с душой. 
Для каждого из членов команды этот совместный проект был первым подобным.

### Техническое описание или приступая к работе:
1. Для работы проекта понадобится предустановленный интерпретатор Python.
2. Для работы проекта понадобятся прямые руки и немного смекалки, elif кривые руки и много смекалки, elif бьющее через край желание пользоваться приложением, которое не имеет практически ничего общего с современными интерфейсами. Straight to retro, так сказать.
3. Для работы проекта понадобится умение запускать и совладать с функционалом командного окна: cmd, PowerShell, GitBash.
- Есть два подхода к работе, которые отличаются разницей в начале работы с приложением и один из которых является более трудоёмким и требуется к исполнению всякий раз, когда вы желаете приступить к работе.
- А второй подразумевает установку пакета по ссылке -- [PyBakers](https://test.pypi.org/project/PyBakers-Mini-Organizer/) . Установка производится командой, которая всеми силами просит скопировать и вставить её в ваше комнадное окно и находится прямо по ссылке в предыдущем предложении.

  ```pip install -i https://test.pypi.org/simple/ PyBakers-Mini-Organizer```
       
4. Если был выбран первый путь, то вы сами его выбрали, на разработчика пенять нечего: прямо здесь, чуть выше этого текста есть синяя кнопочка Code, нажав на которую можно получить доступ ко всем файлам этого репозитория, удобно запакованном в zip-архив и доставленном прямо на ваш ПК.
Открыв его и распаковав в пустую папку, вы можете начинать работу, для этого необходимо запустить командное окно в папке, в которой находится файл executor.py (вместе со всеми остальными, что были с ним в одной папке), после запуска которого необходимо прописать команду: python executor.py. Приложение начнёт (должно начать, у нас начинало) работу, а внутренние подсказки предоставят информацию о функционале. При выборе этого пути, запуск приложения всегда будет подразумевать открытие папки с указанным выше файлом, а для работы функционала file-sorter папку, в которой нужно отсортировать файлы, необходимо будет вложить папку с указанным выше файлом.

5. Если вы человек рассудительный и у вас нет странной тяги к неоправданным ресурсозатратным действиям, то вы выбрали второй путь. 
- И если так, то после установки пакета командой из ссылки выше, вы получите доступ к функционалу программы ИЗ ЛЮБОЙ папки, запустив там командное окно и прописав команду "pybakers".
В таком случае функционал file-sorter будет доступен из папки, в которой был способом, указанным выше, запущен наш проект, а значит все вложенные в эту папку папки включая её саму, попадают под возможности сортировки.

#### Немного об управлении:

Главное меню выполнено на интуитивно понятном уровне, а значит с ним проблем быть не должно. А вот что касается первых двух его пунктов, то здесь есть небольшой свод комманд для каждого.

##### Для phonebook актуальным будет:
- add contact <name> <phone> - adding the record;
- update number <name> <old number> <new number> - updating phone number;
- append number <name> <new number> - adding additional phone number;
- delete number <name> <number> - delete phone number;
- show all - view all saved records;
- show near bd <days from today to> - finding out about upcoming birthdays;
- add email <name> <email> - adding email;
- append email <name> <email> - adding additional email;
- delete email <name> <email> - delete email;
- add birthday <name> <birthday "dd.mm.yyyy"> - adding birthday;
- help - view this help;
- здравствуйте, привет, hello, hi - greetings;
- delete contact <name> - deleting the contact;
- find - searching the record;
- clear, cls - clears the window;
- clear phonebook - clears the phonebook;
- exit, выход, quit, q  - closing the program;

> И вы можете спросить: "Чего?! Ридми весь на русском (даже не на украинском!), а комманды почему-то на английском?!".

> И я отвечу: "**Ну да.**"

##### Для notes акуальным будет:
- "add note" -> to add note, example: add note __Name__ __Note TXT__;
- "delete note" -> to delete note , example: delete note __Name__;
- "change note" -> to change note , example: change note __Name__;
- "add tag" -> to add tag , example: add tag __Name__;
- "change tag" -> to add tag , example: change tag __Name__;
- "delete tag" -> to add tag , example: delete tag __Name__;
- "show all" -> to show all notes;
- "show all #" -> to show all notes in # step;
- "finder" -> to start searching in tags or text;
- "exit" or "." -> to exit;

##### Для file-sorting-utility актуальным будет:
- <.> -- enter dot to exit;

Но куда более важная деталь -- это понимание, что утилита спрашивает от вас наименование папки, в которой должен будет произойти процесс сортировки, а папка эта **ОБЯЗАТЕЛЬНО** должна лежать внутри папки, откуда утилита была запущена.

### Об авторах:

Над данным проектом работали:
- Сергей Сытник/bkitw -- в роли тимлида (не давайте ему писать readme);
- Андрей Васильченко/kidstonek -- в роли стального разработчика (разобрался в тех штуках, в которых не разобрался тимлид);
- Олеся Попиловская/Olesia P -- в роли скрам-мастера, генератора идей и воодушевителя;

[![GitHub Contributors Image](https://contrib.rocks/image?repo=bkitw/project_of_the_5-th)](https://github.com/bkitw)
[![GitHub Contributors Image](https://contrib.rocks/image?repo=Olesia-Usagi/Project_py6)](https://github.com/Olesia-Usagi)
[![GitHub Contributors Image](https://contrib.rocks/image?repo=kidstonek/HW_12)](https://github.com/kidstonek)

### Послесловие:

***Мы очень рады, что вы дочитали этот readme и даже, возможно, собираетесь воспользоваться нашим приложением. Надеемся, что ваш опыт будет положительным, а ощущения исключительно приятными. Всего вам наилучшего и ожидайте новых релизов.***


Link to pip packet: [PyBakers](https://test.pypi.org/project/PyBakers-Mini-Organizer/)
      
pip install command:
  ```pip install -i https://test.pypi.org/simple/ PyBakers-Mini-Organizer```

[![Language](https://img.shields.io/badge/language-python-blue?&style=plastic)](https://www.python.org)
[![Language version](https://img.shields.io/badge/version-3.10-red?&style=plastic)](https://www.python.org/downloads/)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/LeadShadow/CW-Console-Bot?color=black?&style=plastic)
![GitHub Release Date](https://img.shields.io/badge/release--date-june/july-orange?&style=plastic)
![GitHub repo size](https://img.shields.io/badge/repo%20size-≈100%20kB-pink?&style=plastic)



