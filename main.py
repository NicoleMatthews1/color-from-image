from flask import Flask, render_template, request
import colorgram

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

@app.route('/')
@app.route('/index')
def get_all_posts():
    return render_template("index.html")

@app.route("/color", methods=["GET", "POST"])
def get_image():
    if request.method == 'POST':
        if 'image' == "":
            return 'there is no image in form!'
        else:
            image = request.files['image']

            colors = colorgram.extract(image, 6)
            hex_colors = []

            for color in colors:
                r = color.rgb.r
                g = color.rgb.g
                b = color.rgb.b
                new_color = rgb2hex(r, g, b)
                hex_colors.append(new_color)

            print(hex_colors)
            return render_template("color.html", all_colors=hex_colors)

def grab_color():
    colors = colorgram.extract('image.jpg', 20)
    rgb_colors = []


    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = rgb2hex(r, g, b)
        rgb_colors.append((new_color))

    print(rgb_colors)

if __name__ == "__main__":
    app.run(debug=True)
