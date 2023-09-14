In Jinja format, `{{blog.title}}` and `{{blog['title']}}` return the same value because contaxt passed to the template is a dictionary with key-value pairs.
For internal urls, the href tag should be `<a href="{{url_for('about')}}"> About us </a>` there 'about' is a method that returns a template for about us page




