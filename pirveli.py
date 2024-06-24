def create_html():
    def insert_into_html(pirveli, meore, mesame):
        html_content = f"""
        <html>
            <body>
                <h1>{pirveli}</h1>
                <h1>{meore}</h1>
                <p>{mesame}</p>
            </body>
        </html>
        """
        return html_content
    return insert_into_html

# top_order_function = create_html
# html_generator = top_order_function() #asec shveba
html_generator = create_html()
html_output = html_generator("BTU AI", "Tesla AI", "Python AI")
print(html_output)
