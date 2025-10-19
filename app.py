from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    # --- 1. Get all answers from the form ---
    leaves_yellow = request.form.get('leaves_yellow')
    brown_spots = request.form.get('brown_spots')
    direct_sun = request.form.get('direct_sun')
    
    # *** UPDATED LOGIC HERE ***
    # Get the value from our new combined question
    soil_moisture = request.form.get('soil_moisture')
    # *** END OF UPDATE ***

    # --- 2. This is your Knowledge Base (the rules) ---
    
    result = {
        'name': "Unknown",
        'solution': "Sorry, I can't diagnose the problem based on these answers.",
        'reasoning': "No rules were matched.",
        'image': None 
    }

    # *** RULE 1 UPDATED ***
    # Check if soil_moisture is 'wet'
    if leaves_yellow == 'yes' and soil_moisture == 'wet':
        result = {
            'name': "Overwatering",
            'solution': "Let the soil dry out completely. Water less frequently and ensure your pot has drainage holes.",
            'reasoning': "The combination of YELLOW LEAVES and WET SOIL is a classic sign of overwatering, as the roots are suffocating.",
            'image': "overwatered.png"
        }
    
    # Rule 2: Sunburn (no change)
    elif brown_spots == 'yes' and direct_sun == 'yes':
        result = {
            'name': "Sunburn",
            'solution': "Move the plant to a spot with indirect 'bright' light, not direct 'hot' sun. Do not cut off the burnt leaves unless they are fully dead.",
            'reasoning': "BROWN, DRY SPOTS combined with a location in DIRECT SUN indicates the plant's leaves are being scorched.",
            'image': "sunburn.png"
        }

    # *** RULE 3 UPDATED ***
    # Check if soil_moisture is 'dry'
    elif leaves_yellow == 'yes' and soil_moisture == 'dry':
        result = {
            'name': "Underwatering",
            'solution': "Give the plant a deep, thorough watering. Check the soil more frequently and don't let it get bone-dry.",
            'reasoning': "YELLOW LEAVES plus BONE-DRY SOIL suggests the plant is sacrificing its leaves due to a lack of water.",
            'image': "underwatered.png"
        }

    # --- 3. Send the entire 'result' object to the result.html page ---
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)