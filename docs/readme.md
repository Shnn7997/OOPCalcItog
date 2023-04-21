  Для запуска приложения необходимо выполнить следующие шаги:

1. Установить Python 3. Можно скачать его с официального сайта https://www.python.org/downloads/

2. Установить зависимости проекта, выполнив команду pip install -r requirements.txt

3. Запустить приложение, выполнив команду python main.py

Приложение представляет собой калькулятор комплексных чисел, который поддерживает операции сложения, вычитания, умножения, деления и извлечения квадратного корня. Для реализации калькулятора были применены следующие архитектурные паттерны и принципы SOLID:

1. Фабричный метод - для создания объектов класса ComplexNumber был использован фабричный метод, который позволяет создавать объекты, избавляя клиентский код от прямого создания объектов.

2. Принцип единственной ответственности - каждый класс отвечает только за одну функцию, что обеспечивает легкость поддержки и модификации кода.

3. Принцип открытости/закрытости - калькулятор представляет собой закрытую систему, которая может быть расширена путем добавления новых операций без изменения существующего кода.

4. Принцип подстановки Барбары Лисков - класс ComplexNumberFactory является подклассом абстрактного класса, что позволяет использовать его вместо абстрактного класса в клиентском коде.

5. Логирование - для логирования работы калькулятора была использована библиотека logging, которая позволяет записывать сообщения в файл.

6. Разделение кода на модули - каждый класс был вынесен в отдельный файл, что обеспечивает легкость поддержки и модификации кода. Кроме того, были исключены круговые зависимости между модулями.

7. Применение архитектурных паттернов - был использован фабричный метод для создания объектов, что обеспечивает гибкость и расширяемость кода. Кроме того, были использованы классы и наследование для реализации калькулятора.

Таким образом, калькулятор комплексных чисел, реализованный с использованием паттернов проектирования и принципов SOLID, обеспечивает гибкость, расширяемость и легкость поддержки кода. Логирование работы приложения позволяет отслеживать ошибки и улучшать качество кода.