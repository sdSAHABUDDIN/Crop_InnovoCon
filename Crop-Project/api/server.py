from flask import Flask, jsonify,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load
import pickle
from flask_cors import CORS

# Load scaler and model
sc=load('scaler.joblib')
model=pickle.load(open('Crop_model.pkl','rb'))
feature_columns=pickle.load(open('feature_columns.pkl','rb'))

#creating flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/home', methods=['GET'])
def home():
    return jsonify(
        {
            "users": [
                'syed',
                'saha'
            ]
        }
    )

@app.route('/api/predict',methods=['POST'])
def predict_crop():
    # Parse JSON data from the request
    data=request.json
    required_fields=['Nitrogen','Phosphorus','Potassium','Temperature','Humidity','pH','Rainfall']
    
   
    # Validate that all required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        # Extract and convert parameters
        N = int(data['Nitrogen'])
        P=int(data['Phosphorus'])
        K = int(data['Potassium'])
        temperature = float(data['Temperature'])
        humidity=float(data['Humidity'])
        ph=float(data['pH'])
        rainfall=float(data['Rainfall'])

        # Range checks
        if not (0 <= N <= 140):
            return jsonify({"error": f"Nitrogen (N) must be between 0 and 140. You provided {N}"}), 400
        if not (0 <= P <= 145):
            return jsonify({"error": f"Phosphorus (P) must be between 0 and 140. You provided {P}"}), 400
        if not (5 <= K <= 205):
            return jsonify({"error": f"Potassium (K) must be between 5 and 205. You provided {K}"}), 400
        if not (0 <= temperature<= 45):  # Example temp range
            return jsonify({"error": f"Temperature must be between 0 and 50°C. You provided {temperature}"}), 400
        if not (10 <= humidity <= 100):  # Example humidity range
            return jsonify({"error": f"Humidity must be between 10 and 100. You provided {humidity}"}), 400
        if not (3 <= ph <= 9):  # Example pH range
            return jsonify({"error": f"pH must be between 4 and 8. You provided {ph}"}), 400
        if not (20 <= rainfall <= 300):  # Example rainfall range
            return jsonify({"error": f"Rainfall must be between 0 and 300mm. You provided {rainfall}"}), 400

        # print(f"Received values: N={N}, P={P}, K={K}, temp={temperature}, humidity={humidity}, ph={ph}, rainfall={rainfall}")

        custom_input = [[N, P, K, temperature, humidity, ph, rainfall]]
        # print("custom_input:",custom_input)
        custom_input_df = pd.DataFrame(custom_input, columns=feature_columns)
        # print("custom_input_df:",custom_input_df)
        # print(f"custom_input_df shape: {custom_input_df.shape}")
        # print(f"Scaler expected input shape: {sc.mean_.shape}")
        # print(f"Scaler mean: {sc.mean_}")
        # print(f"Scaler scale: {sc.scale_}")
        # print("Loaded feature columns:", feature_columns)
       
        custom_input_scaled = sc.transform(custom_input_df)
        # print("custom_input_scaled:", custom_input_scaled)
        

        custom_prediction = model.predict(custom_input_scaled)
        print("custom_prediction:",custom_prediction)
        predict=custom_prediction[0]
        
         
        crop_dict={1:"Rice",2:"Maize",3:"Jute",4:"Cotton",5:"Coconut",6:"Papaya",
                7:"Orange",8:"Apple",9:"Muskmelon",10:"Watermelon",11:"Grapes",
                12:"Mango",13:"Banana",14:"Pigeonpea",15:"Lentil",16:"Blackgram",
                17:"Mungbean",18:"Mothbean",19:"Pigeonpea",20:"Kidnebean",21:"Chickpea",22:"Coffee"}
        if predict in crop_dict:
            crop=crop_dict[predict]
            result={"prediction": crop}
        else:
            result={"prediction": None, "message": "Sorry, no suitable crop found"}

        # Example processing (modify as needed)
        
        return jsonify(result), 200
    except ValueError:
        return jsonify({"error": "Invalid input values"}), 400  
    
@app.route('/api/cropDetails',methods=['POST'])
def get_crop_details():
    
    my_dict = {
        "rice": {  # Change "Rice" to "rice"
            "selection of rice variety": {
                1: "Choose a variety suited to your region, soil type, and water availability.",
                2:"Consider resistance to pests, diseases, and environmental conditions."
            },
            "field preparation": {
                1: "Plough the field 2-3 times to loosen the soil.",
                2:"Level the field for uniform water distribution.",
                3:"Apply organic manure to enrich the soil."
            },
            "seed selection and treatment": {
                1: "Use about 25-30 kg of seeds per hectare for transplanted rice.",
                2:"Treat seeds with fungicides to prevent diseases.",
                3:"Soak seeds in water to ensure better germination."
            },
            "Sowing and Transplanting":{
                1:"For nurseries: Sow pre-treated seeds in a seedbed.",
                2:"After 20-30 days, transplant seedlings to the main field with a spacing of 20x15 cm."
            },
            "Water Management":{
               1:"Maintain 2-5 cm of water in the field during the growth stage.", 
               2:"Avoid stagnant water to prevent disease."
            },
            "Weed Control":{
                1:"Use manual weeding or apply selective herbicides to control weeds.",
                2:"Weed the field 2-3 times during the crop cycle."
            },
            "Fertilizer Application":{
                1:"Apply nitrogen (N), phosphorus (P), and potassium (K) as per soil test recommendations.",
                2:"Split nitrogen fertilizer into 2-3 doses during planting and tillering stages."
            },
            " Pest and Disease Control":{
                1:"Monitor for common pests like stem borers and leaf hoppers.",
                2:"Use biological controls or eco-friendly pesticides."
            },
            "Harvesting":{
                1:"Harvest when 80-85% of the grains turn golden.",
                2:"Avoid over-ripening to prevent grain shattering."
            },
            "Post-Harvest":{
                1:"Dry the grains to reduce moisture content to 14%.",
                2:"Store grains in a cool, dry place to avoid pest infestations."
            }
    },
        "maize": {
        "selection of maize variety": {
            1: "Choose high-yielding hybrid or open-pollinated varieties suited to your region.",
            2: "Select varieties resistant to pests, diseases, and drought."
        },
        "field preparation": {
            1: "Plough the field 2-3 times to achieve a fine tilth.",
            2: "Incorporate organic manure or compost into the soil.",
            3: "Level the field to ensure uniform seed placement."
        },
        "seed selection and treatment": {
            1: "Use 20-25 kg of seeds per hectare depending on the variety.",
            2: "Treat seeds with fungicides or insecticides to prevent soil-borne diseases.",
            3: "Soak seeds overnight to enhance germination."
        },
        "sowing and spacing": {
            1: "Sow seeds at a depth of 4-5 cm using a seed drill or manually.",
            2: "Maintain a spacing of 60x25 cm for optimal growth and yield."
        },
        "water management": {
            1: "Irrigate immediately after sowing to ensure good germination.",
            2: "Provide water at critical stages such as tasseling, silking, and grain filling."
        },
        "weed control": {
            1: "Perform manual or mechanical weeding 2-3 times during the crop cycle.",
            2: "Apply pre-emergent or post-emergent herbicides as required."
        },
        "fertilizer application": {
            1: "Apply nitrogen (N), phosphorus (P), and potassium (K) based on soil tests.",
            2: "Split nitrogen application into 2-3 doses: at sowing, knee height, and tasseling stages."
        },
        "pest and disease control": {
            1: "Monitor for pests such as stem borers, armyworms, and aphids.",
            2: "Use biopesticides or recommended chemical pesticides to control infestations."
        },
        "harvesting": {
            1: "Harvest when cobs are fully mature, kernels are hard, and the husks are dry.",
            2: "Avoid delayed harvesting to prevent losses due to shattering or pest attacks."
        },
        "post-harvest": {
            1: "Dry the cobs properly to reduce moisture content to around 12-14%.",
            2: "Store maize in airtight containers or silos to prevent pest infestation."
        }
        },
        "jute": {
        "selection of jute variety": {
            1: "Choose high-yielding varieties like JRO 524, JRO 8432, or JRO 66.",
            2: "Select varieties based on climatic conditions and resistance to diseases."
        },
        "field preparation": {
            1: "Plough the field 3-4 times to achieve a fine tilth.",
            2: "Level the field and ensure proper drainage.",
            3: "Apply well-decomposed organic manure to enrich the soil."
        },
        "seed selection and treatment": {
            1: "Use certified seeds for better germination and yield.",
            2: "Treat seeds with fungicides to prevent seed-borne diseases.",
            3: "Soak seeds in water for 24 hours before sowing to enhance germination."
        },
        "sowing and spacing": {
            1: "Sow seeds directly in rows spaced 25-30 cm apart.",
            2: "Maintain a seed rate of 5-6 kg per hectare.",
            3: "Ensure a depth of 2-3 cm for proper germination."
        },
        "water management": {
            1: "Irrigate the field immediately after sowing if rainfall is inadequate.",
            2: "Ensure proper moisture during germination and early growth stages.",
            3: "Avoid waterlogging as it can damage the crop."
        },
        "weed control": {
            1: "Weed the field manually or use mechanical tools 2-3 times during the crop cycle.",
            2: "Apply pre-emergent herbicides to minimize weed growth."
        },
        "fertilizer application": {
            1: "Apply nitrogen (N), phosphorus (P), and potassium (K) based on soil test recommendations.",
            2: "Split nitrogen application into two doses: at sowing and 4 weeks after sowing.",
            3: "Add micronutrients like zinc if the soil is deficient."
        },
        "pest and disease control": {
            1: "Monitor for pests like jute hairy caterpillars and stem weevils.",
            2: "Use biopesticides or neem-based sprays to control pests effectively.",
            3: "Prevent diseases like stem rot by maintaining field hygiene."
        },
        "harvesting": {
            1: "Harvest when plants are 100-120 days old, just before seed formation.",
            2: "Cut the plants close to the ground for maximum yield."
        },
        "retting and fiber extraction": {
            1: "Bundle the harvested plants and immerse them in clean water for retting.",
            2: "Separate fibers by hand or mechanical tools once retting is complete.",
            3: "Wash and dry fibers thoroughly before storage or sale."
        },
        "post-harvest": {
            1: "Grade fibers based on quality before storing or selling.",
            2: "Store fibers in a dry, cool place to prevent deterioration."
        }
        },
        "cotton": {
        "variety selection": {
            1: "Choose varieties based on your region's climate and soil type.",
            2: "Consider fiber quality, yield potential, and disease resistance."
        },
        "soil preparation": {
            1: "Deep plough to 20-30 cm depth for good root development.",
            2: "Create fine tilth through multiple harrowings.",
            3: "Form ridges and furrows for proper drainage."
        },
        "seed treatment": {
            1: "Use 15-20 kg seeds per hectare.",
            2: "Treat seeds with fungicides to prevent seedling diseases.",
            3: "Acid-delint seeds for better germination."
        },
        "sowing": {
            1: "Sow at 4-5 cm depth when soil temperature reaches 18°C.",
            2: "Maintain row spacing of 90-120 cm and plant spacing of 30-45 cm."
        },
        "irrigation": {
            1: "Provide first irrigation 3-4 weeks after sowing.",
            2: "Critical irrigation periods: flowering and boll development.",
            3: "Avoid waterlogging to prevent root rot."
        },
        "weed management": {
            1: "Maintain weed-free conditions for first 60 days.",
            2: "Use inter-row cultivation or approved herbicides."
        },
        "nutrient management": {
            1: "Apply NPK based on soil test results.",
            2: "Split nitrogen application: 40% at sowing, 30% at flowering, 30% at boll formation."
        },
        "pest control": {
            1: "Monitor for bollworms, aphids, and whiteflies.",
            2: "Implement integrated pest management strategies.",
            3: "Use pheromone traps for pest monitoring."
        },
        "harvesting": {
            1: "Pick cotton when bolls are fully opened and dry.",
            2: "Avoid harvesting wet cotton to maintain quality.",
            3: "Multiple pickings may be required as bolls mature."
        },
        "post-harvest": {
            1: "Clean harvested cotton to remove debris.",
            2: "Dry to maintain moisture content below 8-10%.",
            3: "Grade based on fiber quality parameters."
        }
        },
        "coconut": {
    "variety selection": {
        1: "Choose between Tall, Dwarf, or Hybrid varieties based on purpose and region.",
        2: "Consider factors like drought tolerance, disease resistance, and yield potential."
    },
    "site preparation": {
        1: "Clear land and dig pits of 1m × 1m × 1m size.",
        2: "Space pits 7.5-9m apart in triangle or square pattern.",
        3: "Fill pits with topsoil mixed with organic matter and fertilizers."
    },
    "planting material": {
        1: "Select 11-12 month old healthy seedlings.",
        2: "Choose nuts from mother palms with good yield history.",
        3: "Ensure seedlings have 4-5 leaves and are disease-free."
    },
    "planting": {
        1: "Plant seedlings at onset of rainy season.",
        2: "Place seedling in center of pit and fill with soil.",
        3: "Provide shade for young seedlings in initial months."
    },
    "irrigation": {
        1: "Irrigate frequently in first 2 years of establishment.",
        2: "Maintain soil moisture through basin or drip irrigation.",
        3: "Water needs increase during summer months."
    },
    "nutrient management": {
        1: "Apply organic manure twice a year.",
        2: "Provide NPK fertilizers in split doses.",
        3: "Apply micronutrients based on deficiency symptoms."
    },
    "weed control": {
        1: "Maintain clean basin around palm.",
        2: "Use cover crops in inter-row spaces.",
        3: "Practice intercropping where suitable."
    },
    "pest management": {
        1: "Monitor for rhinoceros beetle and red palm weevil.",
        2: "Use pheromone traps and biological controls.",
        3: "Regular crown cleaning to prevent pest buildup."
    },
    "disease control": {
        1: "Watch for bud rot and stem bleeding.",
        2: "Remove and destroy diseased parts.",
        3: "Apply fungicides when necessary."
    },
    "harvesting": {
        1: "Harvest at 11-12 month intervals.",
        2: "Pick fully mature nuts (10-11 months old).",
        3: "Use trained climbers or pole harvesting methods."
    },
    "post-harvest": {
        1: "De-husk nuts within 1-2 days of harvest.",
        2: "Grade nuts based on size and quality.",
        3: "Store in cool, dry conditions if not processing immediately."
    }
    },
        "papaya": {
    "variety selection": {
        1: "Choose between dioecious or gynodioecious varieties.",
        2: "Select varieties based on fruit size, flesh color, and disease resistance.",
        3: "Consider local market preferences and climate adaptability."
    },
    "soil preparation": {
        1: "Prepare well-drained soil with pH 6.0-6.5.",
        2: "Deep plough and create raised beds of 30-45cm height.",
        3: "Add organic matter to improve soil structure."
    },
    "seed preparation": {
        1: "Extract seeds from ripe fruits of healthy plants.",
        2: "Dry seeds in shade and treat with fungicide.",
        3: "Use 250-300g seeds per hectare."
    },
    "planting": {
        1: "Sow 2-3 seeds per pit at 1-2cm depth.",
        2: "Maintain spacing of 2m × 2m or 2.5m × 2.5m.",
        3: "Thin to one seedling per pit after 45-60 days."
    },
    "irrigation": {
        1: "Provide regular irrigation during establishment.",
        2: "Maintain consistent soil moisture without waterlogging.",
        3: "Reduce irrigation during fruit ripening."
    },
    "nutrient management": {
        1: "Apply balanced NPK fertilizer monthly.",
        2: "Provide additional nitrogen during vegetative growth.",
        3: "Add micronutrients, especially boron and zinc."
    },
    "weed control": {
        1: "Maintain weed-free basin around plants.",
        2: "Use mulching to suppress weed growth.",
        3: "Avoid deep cultivation near roots."
    },
    "pest management": {
        1: "Monitor for mites, fruit flies, and mealy bugs.",
        2: "Use sticky traps and fruit wrapping.",
        3: "Apply approved pesticides when necessary."
    },
    "disease control": {
        1: "Watch for virus diseases like PRSV and leaf spots.",
        2: "Remove infected plants immediately.",
        3: "Maintain field sanitation."
    },
    "harvesting": {
        1: "Harvest when fruits show 25-50% yellow coloration.",
        2: "Begin harvesting 8-9 months after planting.",
        3: "Pick fruits carefully to avoid latex staining."
    },
    "post-harvest": {
        1: "Grade fruits based on size and maturity.",
        2: "Store at 13°C with 85-90% relative humidity.",
        3: "Handle fruits gently to prevent bruising."
    }
    },
        "orange": {
    "variety selection": {
        1: "Choose varieties based on climate and market demand (Valencia, Navel, etc.).",
        2: "Select rootstock suited to soil type and disease resistance.",
        3: "Consider fruit quality, yield potential, and maturity period."
    },
    "site preparation": {
        1: "Ensure well-drained soil with pH 6.0-7.0.",
        2: "Dig pits of 60cm × 60cm × 60cm size.",
        3: "Space pits 5-6m apart depending on variety."
    },
    "planting material": {
        1: "Use certified disease-free nursery plants.",
        2: "Select budded plants 12-18 months old.",
        3: "Ensure plants show good graft union and vigor."
    },
    "planting": {
        1: "Plant at beginning of rainy season or spring.",
        2: "Place grafted portion above ground level.",
        3: "Provide stake support to young plants."
    },
    "irrigation": {
        1: "Maintain regular irrigation schedule.",
        2: "Critical periods: flowering, fruit set, and development.",
        3: "Use drip irrigation for water efficiency."
    },
    "nutrient management": {
        1: "Apply organic manure before planting.",
        2: "Provide NPK in split doses annually.",
        3: "Spray micronutrients, especially zinc and manganese."
    },
    "pruning": {
        1: "Remove water sprouts and crossed branches.",
        2: "Maintain tree height for easy harvesting.",
        3: "Thin out dense canopy for light penetration."
    },
    "pest control": {
        1: "Monitor for citrus psylla, fruit flies, and scales.",
        2: "Use integrated pest management approaches.",
        3: "Apply pest-specific controls when needed."
    },
    "disease management": {
        1: "Watch for citrus canker, greening, and tristeza.",
        2: "Remove infected parts promptly.",
        3: "Use preventive copper sprays during wet season."
    },
    "harvesting": {
        1: "Pick fruits when fully colored and mature.",
        2: "Clip fruits with small stem portion attached.",
        3: "Avoid harvesting during wet conditions."
    },
    "post-harvest": {
        1: "Clean and grade fruits by size and quality.",
        2: "Store at 4-7°C with 85-90% relative humidity.",
        3: "Wax fruits if required for long-distance marketing."
    },
    "orchard floor management": {
        1: "Maintain clean basin around tree trunk.",
        2: "Use cover crops in inter-row spaces.",
        3: "Apply mulch to conserve moisture."
    }
    },
        "muskmelon": {
    "variety selection": {
      1: "Choose varieties based on local climate, market preference (e.g., cantaloupe, honeydew, netted, smooth-skinned).",
      2: "Consider disease resistance (e.g., Fusarium wilt, powdery mildew).",
      3: "Select for desired fruit size, shape, sweetness, and maturity period (early, mid, or late-season)."
    },
    "site preparation": {
      1: "Select well-drained, sandy loam soil with a pH of 6.0-6.8.",
      2: "Ensure full sun exposure (at least 6-8 hours per day).",
      3: "Prepare raised beds or hills to improve drainage and soil warming."
    },
    "planting material": {
      1: "Use high-quality seeds from reputable suppliers.",
      2: "Start seeds indoors 3-4 weeks before the last expected frost or direct sow after the soil has warmed.",
      3: "Consider using transplants for earlier harvests in cooler climates."
    },
    "planting": {
      1: "Direct sow seeds 1 inch deep and 2-3 feet apart in rows 4-6 feet apart.",
      2: "Transplant seedlings after the danger of frost has passed, spacing them 2-3 feet apart.",
      3: "Avoid disturbing the roots when transplanting."
    },
    "irrigation": {
      1: "Provide consistent and regular watering, especially during fruit development.",
      2: "Water at the base of the plants to avoid wetting the foliage, which can promote disease.",
      3: "Use drip irrigation or soaker hoses for efficient water use.",
      4: "Reduce watering as fruits approach maturity to improve sweetness."
    },
    "nutrient management": {
      1: "Incorporate compost or well-rotted manure before planting.",
      2: "Apply a balanced fertilizer (e.g., 10-10-10) at planting and side-dress with nitrogen fertilizer during vine growth and fruit set.",
      3: "Avoid excessive nitrogen, which can promote vine growth at the expense of fruit production."
    },
    "pruning": {
      1: "Pinch off lateral vines to encourage the development of the main vine and fruit.",
      2: "Remove any diseased or damaged leaves or vines.",
      3: "Some growers prune to a specific number of fruits per vine to improve fruit size and quality (optional)."
    },
    "pest control": {
      1: "Monitor for cucumber beetles, aphids, squash bugs, and vine borers.",
      2: "Use row covers to protect young plants from pests.",
      3: "Employ integrated pest management (IPM) strategies, including handpicking, traps, and targeted insecticide applications if necessary."
    },
    "disease management": {
      1: "Watch for powdery mildew, downy mildew, Fusarium wilt, and bacterial wilt.",
      2: "Practice crop rotation and avoid planting melons in the same area year after year.",
      3: "Use disease-resistant varieties and apply fungicides as needed.",
      4: "Ensure good air circulation to reduce humidity and disease pressure."
    },
    "harvesting": {
      1: "Harvest muskmelons when they slip easily from the vine (full slip) or when the stem begins to crack around the fruit.",
      2: "The rind color will also change, and the fruit will emit a sweet aroma.",
      3: "Avoid bruising the fruit during harvest."
    },
    "post-harvest": {
      1: "Handle harvested melons carefully to prevent bruising.",
      2: "Store at cool temperatures (45-50°F or 7-10°C) and high humidity (85-95%) for short-term storage.",
      3: "Muskmelons are best consumed soon after harvest for optimal flavor and texture."
    },
    "orchard floor management": {
      1: "Use black plastic mulch to warm the soil, conserve moisture, and suppress weeds.",
      2: "Alternatively, use organic mulch such as straw or hay.",
      3: "Keep the area around the plants weed-free."
    }
  },
        "apple": {
    "variety selection": {
        1: "Choose varieties based on chilling hours requirement and local climate.",
        2: "Select suitable pollinizer varieties for cross-pollination.",
        3: "Consider disease resistance, fruit quality, and market demand."
    },
    "site preparation": {
        1: "Select well-drained soil with pH 6.0-6.8.",
        2: "Dig pits of 1m × 1m × 1m at proper spacing.",
        3: "Ensure good air drainage to prevent frost damage."
    },
    "planting material": {
        1: "Use certified virus-free grafted plants.",
        2: "Select 1-2 year old healthy plants.",
        3: "Choose appropriate rootstock for desired tree size."
    },
    "planting": {
        1: "Plant during dormant season (late fall to early spring).",
        2: "Space trees 3-5m apart depending on rootstock.",
        3: "Ensure graft union is above ground level."
    },
    "training and pruning": {
        1: "Train young trees to modified central leader system.",
        2: "Prune annually during dormant season.",
        3: "Maintain open canopy for light penetration."
    },
    "nutrient management": {
        1: "Apply balanced NPK based on soil tests.",
        2: "Provide regular calcium sprays for fruit quality.",
        3: "Add micronutrients, especially boron and zinc."
    },
    "irrigation": {
        1: "Maintain consistent soil moisture.",
        2: "Critical periods: fruit set and development.",
        3: "Avoid over-irrigation near harvest."
    },
    "pest control": {
        1: "Monitor for codling moth, apple maggot, and mites.",
        2: "Use pheromone traps and mating disruption.",
        3: "Apply integrated pest management strategies."
    },
    "disease management": {
        1: "Control apple scab, fire blight, and powdery mildew.",
        2: "Apply preventive fungicide sprays.",
        3: "Maintain orchard sanitation."
    },
    "fruit thinning": {
        1: "Thin fruits 30-40 days after full bloom.",
        2: "Leave one fruit per cluster.",
        3: "Adjust crop load based on tree vigor."
    },
    "harvesting": {
        1: "Check fruit maturity using starch-iodine test.",
        2: "Harvest with stem attached to prevent damage.",
        3: "Pick during cool hours of the day."
    },
    "post-harvest": {
        1: "Pre-cool fruits immediately after harvest.",
        2: "Store at 0-4°C with 90-95% relative humidity.",
        3: "Grade and pack according to market standards."
    }
    },
        "watermelon": {
    "variety selection": {
        1: "Choose between seeded or seedless varieties based on market demand.",
        2: "Select varieties for disease resistance and fruit size.",
        3: "Consider rind thickness for transportation needs."
    },
    "soil preparation": {
        1: "Prepare well-drained sandy loam soil with pH 6.0-6.8.",
        2: "Form raised beds 15-20cm high and 1.5-2m wide.",
        3: "Add organic matter to improve soil structure."
    },
    "seed preparation": {
        1: "Use 2-3 kg seeds per hectare for direct sowing.",
        2: "Treat seeds with fungicide before sowing.",
        3: "For seedless varieties, include pollinator plants."
    },
    "planting": {
        1: "Sow seeds 2-3cm deep when soil temperature reaches 20°C.",
        2: "Space plants 1.5-2m between rows and 0.6-1m within rows.",
        3: "Use plastic mulch for weed control and soil warming."
    },
    "irrigation": {
        1: "Maintain consistent soil moisture during vine growth.",
        2: "Critical irrigation during flowering and fruit development.",
        3: "Reduce water 1-2 weeks before harvest for better sweetness."
    },
    "nutrient management": {
        1: "Apply balanced NPK fertilizer before planting.",
        2: "Side-dress with nitrogen at vine running stage.",
        3: "Provide potassium for improved fruit quality."
    },
    "vine management": {
        1: "Train vines for proper spacing.",
        2: "Prune excessive vegetative growth.",
        3: "Turn fruits occasionally to prevent yellow spots."
    },
    "pest control": {
        1: "Monitor for aphids, cucumber beetles, and spider mites.",
        2: "Use row covers until flowering.",
        3: "Apply insecticides only when necessary."
    },
    "disease management": {
        1: "Watch for powdery mildew, anthracnose, and fusarium wilt.",
        2: "Maintain good air circulation.",
        3: "Apply preventive fungicides during humid conditions."
    },
    "pollination": {
        1: "Place beehives for adequate pollination.",
        2: "Remove row covers during flowering.",
        3: "Best fruit set occurs with 8-10 bee visits per flower."
    },
    "harvesting": {
        1: "Check maturity by yellow ground spot and dried tendril.",
        2: "Harvest when fruit gives hollow sound when tapped.",
        3: "Cut stem with sharp knife leaving 2-3cm attached."
    },
    "post-harvest": {
        1: "Store at 10-15°C with 85-90% relative humidity.",
        2: "Handle fruits carefully to prevent cracking.",
        3: "Market immediately for best quality."
    }
    },  
        "grapes": {
    "variety selection": {
      1: "Choose varieties suitable for your climate (e.g., cold-hardy for northern regions, heat-tolerant for warmer areas).",
      2: "Consider intended use (table grapes, wine grapes, juice grapes, raisin grapes).",
      3: "Select for disease resistance (e.g., powdery mildew, downy mildew, black rot).",
      4: "Consider fruit characteristics (e.g., color, size, flavor, seedlessness)."
    },
    "site preparation": {
      1: "Select a site with full sun exposure (at least 7-8 hours per day).",
      2: "Ensure well-drained soil with a pH of 6.0-7.0.",
      3: "Avoid low-lying areas prone to frost pockets or waterlogging.",
      4: "Prepare the soil by deep tilling or digging to improve drainage and root penetration.",
      5: "Install a trellis or support system before planting."
    },
    "planting material": {
      1: "Use certified disease-free grapevines from reputable nurseries.",
      2: "Select dormant, bare-root vines or potted vines.",
      3: "Consider grafted vines for improved disease resistance or adaptation to specific soil conditions."
    },
    "planting": {
      1: "Plant in early spring after the danger of frost has passed.",
      2: "Dig holes large enough to accommodate the root system without crowding.",
      3: "Plant vines at the same depth they were grown in the nursery.",
      4: "Space vines according to the variety and training system (typically 6-8 feet apart).",
      5: "Water thoroughly after planting."
    },
    "irrigation": {
      1: "Water regularly during the first year to establish a strong root system.",
      2: "Mature vines are relatively drought-tolerant but benefit from supplemental irrigation during dry periods, especially during fruit development.",
      3: "Use drip irrigation or soaker hoses to avoid wetting the foliage and reduce disease risk.",
      4: "Avoid overwatering, which can lead to root rot."
    },
    "nutrient management": {
      1: "Conduct a soil test to determine nutrient needs.",
      2: "Apply a balanced fertilizer in early spring before bud break.",
      3: "Side-dress with nitrogen fertilizer during active growth.",
      4: "Avoid excessive nitrogen, which can promote vegetative growth at the expense of fruit production.",
      5: "Apply micronutrients as needed based on soil test results."
    },
    "pruning": {
      1: "Pruning is essential for grape production and vine health.",
      2: "Prune annually during the dormant season (late winter or early spring).",
      3: "Choose a training system (e.g., cane pruning, spur pruning) appropriate for the variety.",
      4: "Remove dead, damaged, and diseased wood.",
      5: "Maintain a balanced vine structure for optimal fruit production and air circulation."
    },
    "pest control": {
      1: "Monitor for common grape pests such as aphids, grape berry moths, Japanese beetles, and phylloxera.",
      2: "Use integrated pest management (IPM) strategies, including cultural practices, biological controls, and targeted insecticide applications if necessary.",
      3: "Protect developing fruit from birds and other wildlife using netting or other deterrents."
    },
    "disease management": {
      1: "Watch for common grape diseases such as powdery mildew, downy mildew, black rot, and Botrytis bunch rot.",
      2: "Practice good sanitation by removing fallen leaves and pruning debris.",
      3: "Ensure good air circulation through proper pruning and vine training.",
      4: "Apply fungicides as needed for disease prevention and control.",
      5: "Choose disease-resistant varieties whenever possible."
    },
    "harvesting": {
      1: "Harvest grapes when they reach the desired ripeness for their intended use.",
      2: "Table grapes are typically harvested when they reach full color and sweetness.",
      3: "Wine grapes are harvested based on sugar content, acidity, and other factors.",
      4: "Use pruning shears or grape harvesting knives to clip clusters from the vine.",
      5: "Handle grapes carefully to avoid bruising."
    },
    "post-harvest": {
      1: "Handle harvested grapes gently to prevent damage.",
      2: "Cool grapes quickly after harvest to maintain quality.",
      3: "Table grapes can be stored for a short period at cool temperatures (32-35°F or 0-2°C) and high humidity (90-95%).",
      4: "Wine grapes are typically processed immediately after harvest."
    },
    "vineyard floor management": {
      1: "Maintain a weed-free area around the base of the vines.",
      2: "Use cover crops in the inter-row spaces to improve soil health and suppress weeds.",
      3: "Mulch can be used to conserve moisture and suppress weeds.",
      4: "Consider using a vineyard floor management system that suits your specific needs and growing conditions."
    }
  }, 
        "banana": {
    "variety selection": {
      1: "Choose varieties adapted to your climate (tropical or subtropical).",
      2: "Consider market demand and consumer preferences (e.g., Cavendish, Plantain, Red Dacca).",
      3: "Select for disease resistance, especially to Panama disease (Fusarium wilt) and Black Sigatoka.",
      4: "Consider fruit size, yield potential, and growth habit (dwarf, semi-dwarf, tall)."
    },
    "site preparation": {
      1: "Select a site with full sun (at least 6 hours per day) and protection from strong winds.",
      2: "Ensure well-drained soil rich in organic matter with a pH of 6.0-7.5.",
      3: "Prepare the soil by deep digging or plowing to improve drainage and aeration.",
      4: "Incorporate compost or well-rotted manure to enhance soil fertility.",
      5: "Clear the area of weeds and debris."
    },
    "planting material": {
      1: "Use disease-free planting material such as suckers (sword suckers or water suckers) or tissue-cultured plantlets.",
      2: "Select healthy, vigorous suckers from disease-free mother plants.",
      3: "Treat suckers with a fungicide to prevent soilborne diseases.",
      4: "Tissue-cultured plantlets offer disease-free planting material and uniform growth."
    },
    "planting": {
      1: "Plant in the rainy season or at the beginning of the wet season.",
      2: "Dig holes large enough to accommodate the root system (approximately 30-45 cm deep and wide).",
      3: "Space plants according to the variety and desired planting density (typically 2-3 meters apart).",
      4: "Plant suckers at the same depth they were growing previously, ensuring the corm is covered with soil.",
      5: "Water thoroughly after planting."
    },
    "irrigation": {
      1: "Bananas require consistent moisture, especially during periods of active growth and fruit development.",
      2: "Irrigate regularly, especially during dry periods.",
      3: "Use drip irrigation or micro-sprinklers for efficient water use.",
      4: "Avoid overwatering, which can lead to root rot.",
      5: "Mulching helps conserve soil moisture and reduce weed growth."
    },
    "nutrient management": {
      1: "Bananas are heavy feeders and require substantial amounts of nutrients.",
      2: "Apply organic manure or compost regularly to improve soil fertility.",
      3: "Use a balanced fertilizer (e.g., NPK 10-10-10 or similar) in split applications throughout the growing season.",
      4: "Apply micronutrients as needed based on soil and leaf analysis.",
      5: "Potassium is particularly important for fruit development and quality."
    },
    "pruning": {
      1: "Remove excess suckers (desuckering) to maintain a manageable plant density and promote the growth of the main plant.",
      2: "Remove dead or damaged leaves.",
      3: "After harvesting the fruit bunch, cut down the pseudostem to encourage the growth of a new sucker.",
      4: "Remove the male bud (inflorescence) after the last female hand has emerged (dehanding)."
    },
    "pest control": {
      1: "Monitor for common banana pests such as banana weevil borer, nematodes, and aphids.",
      2: "Use integrated pest management (IPM) strategies, including cultural practices, biological controls, and targeted insecticide applications if necessary.",
      3: "Practice good sanitation by removing crop debris and weeds.",
      4: "Use nematode-resistant varieties or soil treatments to manage nematode infestations."
    },
    "disease management": {
      1: "Watch for common banana diseases such as Panama disease (Fusarium wilt), Black Sigatoka, and bunchy top virus.",
      2: "Plant disease-resistant varieties whenever possible.",
      3: "Practice good sanitation and remove infected plants promptly.",
      4: "Use fungicides as needed for disease prevention and control.",
      5: "Quarantine new planting material to prevent the introduction of new diseases."
    },
    "harvesting": {
      1: "Harvest bananas when they reach the mature green stage (approximately 75-80% full).",
      2: "The fruit should be plump and the ridges on the fruit should be less prominent.",
      3: "Cut the entire bunch from the pseudostem using a sharp knife or machete.",
      4: "Handle the bunches carefully to avoid bruising the fruit."
    },
    "post-harvest": {
      1: "Transport harvested bunches carefully to the packing shed.",
      2: "Wash and clean the fruit.",
      3: "Dehand the bunches into individual hands or clusters.",
      4: "Treat the cut ends with a fungicide to prevent post-harvest decay.",
      5: "Pack the fruit in boxes or cartons for transport and marketing.",
      6: "Control ripening using ethylene gas in ripening rooms for commercial markets."
    },
    "plantation floor management": {
      1: "Maintain a weed-free area around the base of the plants.",
      2: "Use cover crops or intercropping to improve soil health and suppress weeds.",
      3: "Apply mulch to conserve moisture and suppress weeds.",
      4: "Ensure good drainage to prevent waterlogging.",
      5: "Regularly remove crop debris and dead leaves to reduce pest and disease pressure."
    }
  },   
        "pigeonpea": {
    "variety selection": {
        1: "Choose between early (120-150 days), medium (150-180 days), or late maturing (180-220 days) varieties.",
        2: "Select varieties based on local climate and disease resistance.",
        3: "Consider plant height and branching habit for intercropping."
    },
    "soil preparation": {
        1: "Prepare well-drained soil with pH 6.5-7.5.",
        2: "Plough land 2-3 times to achieve fine tilth.",
        3: "Form ridges and furrows for better drainage."
    },
    "seed treatment": {
        1: "Use 15-20 kg seeds per hectare.",
        2: "Treat seeds with Rhizobium culture and fungicide.",
        3: "Ensure seed viability through germination test."
    },
    "sowing": {
        1: "Sow at 4-5 cm depth at onset of monsoon.",
        2: "Maintain row spacing of 60-75 cm and plant spacing of 20-25 cm.",
        3: "Consider intercropping with short duration crops."
    },
    "irrigation": {
        1: "Provide irrigation at critical stages: flowering and pod development.",
        2: "Avoid water stagnation at any growth stage.",
        3: "Ensure adequate soil moisture during pod filling."
    },
    "nutrient management": {
        1: "Apply basal dose of phosphorus and potassium.",
        2: "Top dress with nitrogen if needed.",
        3: "Apply micronutrients based on soil test."
    },
    "weed control": {
        1: "Critical weed-free period is first 45-60 days.",
        2: "Use pre-emergence herbicides or manual weeding.",
        3: "Maintain clean field through intercultivation."
    },
    "pest management": {
        1: "Monitor for pod borers, pod fly, and leaf webbers.",
        2: "Use pheromone traps and biological controls.",
        3: "Apply need-based pesticide sprays."
    },
    "disease control": {
        1: "Watch for wilt, sterility mosaic, and phytophthora.",
        2: "Remove and destroy diseased plants.",
        3: "Use resistant varieties in endemic areas."
    },
    "harvesting": {
        1: "Harvest when 80% pods turn brown.",
        2: "Cut plants at base or harvest mature pods.",
        3: "Dry harvested plants/pods in sun."
    },
    "post-harvest": {
        1: "Thresh dried plants mechanically or manually.",
        2: "Clean and grade seeds.",
        3: "Store at 10-12% moisture in airtight containers."
    },
    "cropping system": {
        1: "Suitable for intercropping with cereals or short-duration pulses.",
        2: "Practice crop rotation with cereals.",
        3: "Consider ratoon cropping where suitable."
    }
},
        "lentil": {
    "selection of variety": {
        1: "Choose varieties suited to your region like Masoor, Pusa, or Laird.",
        2: "Select resistant varieties for pests and diseases, and those with good market demand."
    },
    "site selection and soil preparation": {
        1: "Grow lentils in well-drained, loamy soil with a pH range of 6.0-7.5.",
        2: "Prepare the field by ploughing 2-3 times and leveling it.",
        3: "Apply organic manure or compost to enrich the soil."
    },
    "sowing": {
        1: "Sow seeds during the rabi season (November to December).",
        2: "Plant seeds 2-3 cm deep and maintain spacing of 15-20 cm between plants.",
        3: "Use a seed rate of 40-45 kg per hectare."
    },
    "irrigation management": {
        1: "Lentils require light irrigation, water the field 2-3 times during dry spells.",
        2: "Avoid waterlogging as lentils are sensitive to excess moisture."
    },
    "weed control": {
        1: "Use manual weeding or herbicides to control weeds during the early stages.",
        2: "Keep the field free from weeds, especially during the flowering period."
    },
    "fertilizer application": {
        1: "Apply nitrogen, phosphorus, and potassium based on soil test recommendations.",
        2: "Avoid excessive nitrogen as lentils are nitrogen-fixing plants."
    },
    "pest and disease control": {
        1: "Monitor for pests like aphids, lentil weevils, and pod borer.",
        2: "Use neem-based insecticides or biopesticides to control pests.",
        3: "Prevent fungal diseases like rust and blight by applying fungicides as necessary."
    },
    "flowering and pod formation": {
        1: "Maintain optimal moisture levels during flowering to ensure proper pod formation.",
        2: "Ensure good pollination for better pod set."
    },
    "harvesting": {
        1: "Harvest lentils when the pods turn brown and the seeds rattle inside.",
        2: "Cut the plants at the base and allow them to dry in the field for 4-5 days."
    },
    "post-harvest management": {
        1: "Thresh the dried plants carefully to separate the seeds from the pods.",
        2: "Store lentil seeds in a cool, dry place in airtight containers.",
        3: "Clean and grade seeds to remove damaged or underdeveloped ones."
    }
    },
        "blackgram": {
    "variety selection": {
      1: "Choose high-yielding varieties adapted to the local agro-climatic conditions.",
      2: "Consider disease and pest resistance, especially to yellow mosaic virus (YMV) and Cercospora leaf spot.",
      3: "Select varieties with desirable seed characteristics (e.g., seed size, color, and cooking quality).",
      4: "Consider the duration of the variety (early, medium, or late maturing) based on the cropping system."
    },
    "site preparation": {
      1: "Select well-drained loamy to sandy loam soils with a pH of 6.5-7.5.",
      2: "Avoid waterlogged or heavy clay soils.",
      3: "Prepare a fine seedbed by plowing or harrowing 2-3 times followed by leveling.",
      4: "Incorporate well-rotted farmyard manure (FYM) or compost during land preparation to improve soil fertility and water holding capacity."
    },
    "planting material": {
      1: "Use certified, disease-free seeds from reliable sources.",
      2: "Treat seeds with a fungicide (e.g., thiram or carbendazim) to protect against seedborne diseases.",
      3: "Inoculate seeds with Rhizobium culture to enhance nitrogen fixation.",
      4: "Ensure good seed viability by conducting a germination test before sowing."
    },
    "planting": {
      1: "Sow seeds after the first monsoon showers or when sufficient soil moisture is available.",
      2: "The optimal sowing time varies depending on the region and cropping system (e.g., kharif, rabi, or summer).",
      3: "Use a seed drill or sow manually in rows with a spacing of 30-45 cm between rows and 10-15 cm between plants.",
      4: "Sow seeds at a depth of 3-4 cm.",
      5: "Maintain a plant population of approximately 30-40 plants per square meter."
    },
    "irrigation": {
      1: "Blackgram is generally grown as a rainfed crop, but supplemental irrigation can significantly increase yields, especially during dry spells.",
      2: "Provide irrigation at critical growth stages such as flowering and pod filling.",
      3: "Avoid waterlogging, as it can lead to root rot and other diseases.",
      4: "Use efficient irrigation methods like furrow or sprinkler irrigation."
    },
    "nutrient management": {
      1: "Apply basal dose of FYM or compost during land preparation.",
      2: "Apply recommended doses of nitrogen (N), phosphorus (P), and potassium (K) fertilizers based on soil test results.",
      3: "Phosphorus is particularly important for root development and nodulation.",
      4: "Apply fertilizers as basal or top dressing depending on the nutrient and soil conditions.",
      5: "Avoid excessive nitrogen application, as it can promote vegetative growth and reduce pod setting."
    },
    "weed control": {
      1: "Weed control is crucial during the initial growth stages of blackgram.",
      2: "Perform 2-3 hand weedings or use pre-emergence or post-emergence herbicides to control weeds effectively.",
      3: "Intercultural operations like hoeing can also help in weed control and soil aeration.",
      4: "Maintain a clean field to reduce weed competition for nutrients, water, and sunlight."
    },
    "pest control": {
      1: "Monitor for common blackgram pests such as aphids, pod borers, and whiteflies.",
      2: "Use integrated pest management (IPM) practices, including cultural, biological, and chemical methods.",
      3: "Use recommended insecticides judiciously when pest populations reach economic threshold levels.",
      4: "Encourage natural enemies of pests like ladybugs and lacewings."
    },
    "disease management": {
      1: "Watch for common blackgram diseases such as yellow mosaic virus (YMV), Cercospora leaf spot, and root rot.",
      2: "Plant disease-resistant varieties whenever possible.",
      3: "Practice crop rotation to break disease cycles.",
      4: "Remove and destroy infected plants to prevent disease spread.",
      5: "Use recommended fungicides for disease control if necessary."
    },
    "harvesting": {
      1: "Harvest blackgram when the pods turn yellowish-brown and the seeds are mature and dry.",
      2: "Harvesting can be done manually by uprooting the plants or using mechanical harvesters.",
      3: "Dry the harvested plants in the sun for a few days to reduce moisture content.",
      4: "Thresh the dried plants to separate the seeds from the pods."
    },
    "post-harvest": {
      1: "Clean the harvested seeds to remove debris, broken seeds, and other impurities.",
      2: "Dry the cleaned seeds to a safe moisture level (around 10-12%) to prevent storage losses.",
      3: "Store the dried seeds in clean, dry, and airtight containers or bags in a cool and dry place.",
      4: "Protect stored seeds from insect pests and rodents."
    },
      "crop rotation": {
        1: "Rotate blackgram with non-leguminous crops like cereals (e.g., sorghum, maize) to improve soil fertility and reduce pest and disease buildup.",
        2: "Avoid continuous cropping of legumes in the same field.",
        3: "Include blackgram in crop rotation systems to enhance soil health and overall farm productivity."
      }
  },
        "mungbean": {
    "variety selection": {
      1: "Choose high-yielding varieties suitable for the local climate and growing season (kharif, rabi, or summer).",
      2: "Consider disease resistance, especially to yellow mosaic virus (YMV), Cercospora leaf spot, and powdery mildew.",
      3: "Select varieties with desirable seed characteristics (e.g., seed size, color, and cooking quality).",
      4: "Consider the duration of the variety (early, medium, or late maturing) based on the cropping system and available growing period."
    },
    "site preparation": {
      1: "Select well-drained loamy to sandy loam soils with a pH of 6.5-7.5.",
      2: "Avoid waterlogged or heavy clay soils, as they can lead to poor germination and root rot.",
      3: "Prepare a fine seedbed by plowing or harrowing 2-3 times followed by leveling to ensure good seed-soil contact.",
      4: "Incorporate well-rotted farmyard manure (FYM) or compost during land preparation to improve soil fertility and water retention."
    },
    "planting material": {
      1: "Use certified, disease-free seeds from reputable sources.",
      2: "Treat seeds with a fungicide (e.g., thiram or carbendazim) to protect against seedborne diseases and improve germination.",
      3: "Inoculate seeds with Rhizobium culture (specific to mungbean) to enhance nitrogen fixation and reduce the need for nitrogen fertilizers.",
      4: "Ensure good seed viability by conducting a germination test before sowing."
    },
    "planting": {
      1: "Sow seeds after the first monsoon showers (for kharif) or when sufficient soil moisture is available (for rabi and summer).",
      2: "The optimal sowing time varies depending on the region and cropping system.",
      3: "Use a seed drill or sow manually in rows with a spacing of 30-45 cm between rows and 10-15 cm between plants within a row.",
      4: "Sow seeds at a depth of 3-4 cm to ensure good germination and emergence.",
      5: "Maintain a plant population of approximately 30-40 plants per square meter for optimal yield."
    },
    "irrigation": {
      1: "Mungbean is relatively drought-tolerant but responds well to irrigation, especially during critical growth stages like flowering and pod filling.",
      2: "Provide irrigation as needed, especially during dry spells or periods of moisture stress.",
      3: "Avoid waterlogging, as it can lead to root rot and other diseases.",
      4: "Use efficient irrigation methods like furrow, sprinkler, or drip irrigation to conserve water."
    },
    "nutrient management": {
      1: "Apply a basal dose of FYM or compost during land preparation to improve soil organic matter and nutrient availability.",
      2: "Apply recommended doses of phosphorus (P) and potassium (K) fertilizers based on soil test results.",
      3: "Nitrogen fertilizer is generally not required if seeds are properly inoculated with Rhizobium.",
      4: "If nitrogen deficiency is observed, a small dose of nitrogen fertilizer can be applied as a top dressing.",
      5: "Avoid excessive nitrogen application, as it can promote vegetative growth and reduce pod setting."
    },
    "weed control": {
      1: "Weed control is critical during the initial growth stages of mungbean to prevent competition for resources.",
      2: "Perform 1-2 hand weedings or use pre-emergence or post-emergence herbicides to control weeds effectively.",
      3: "Intercultural operations like hoeing can also help in weed control and improve soil aeration.",
      4: "Maintain a clean field to minimize weed pressure and maximize yield."
    },
    "pest control": {
      1: "Monitor for common mungbean pests such as aphids, pod borers, whiteflies, and bean weevils (during storage).",
      2: "Use integrated pest management (IPM) strategies, including cultural, biological, and chemical methods, to manage pests effectively.",
      3: "Use recommended insecticides judiciously when pest populations reach economic threshold levels to minimize environmental impact.",
      4: "Store harvested seeds properly to prevent damage from storage pests like bean weevils."
    },
    "disease management": {
      1: "Watch for common mungbean diseases such as yellow mosaic virus (YMV), Cercospora leaf spot, powdery mildew, and root rot.",
      2: "Plant disease-resistant varieties whenever possible to minimize disease incidence.",
      3: "Practice crop rotation to break disease cycles and reduce pathogen buildup in the soil.",
      4: "Remove and destroy infected plants promptly to prevent disease spread.",
      5: "Use recommended fungicides for disease control if necessary, following label instructions carefully."
    },
    "harvesting": {
      1: "Harvest mungbean when the pods turn yellowish-brown and the seeds are mature and dry.",
      2: "Harvesting can be done manually by uprooting the plants or by picking the mature pods.",
      3: "Dry the harvested plants or pods in the sun for a few days to reduce moisture content before threshing.",
      4: "Thresh the dried plants or pods to separate the seeds from the pods and other plant debris."
    },
    "post-harvest": {
      1: "Clean the harvested seeds to remove debris, broken seeds, and other impurities.",
      2: "Dry the cleaned seeds to a safe moisture level (around 10-12%) to prevent storage losses due to mold and insect infestation.",
      3: "Store the dried seeds in clean, dry, and airtight containers or bags in a cool and dry place, protected from pests and rodents.",
      4: "Fumigate stored seeds if necessary to control storage pests like bean weevils."
    },
    "crop rotation": {
      1: "Rotate mungbean with non-leguminous crops like cereals (e.g., sorghum, maize, wheat) to improve soil fertility and reduce pest and disease buildup.",
      2: "Avoid continuous cropping of legumes in the same field to prevent soil nutrient depletion and disease accumulation.",
      3: "Include mungbean in crop rotation systems to enhance soil health, improve biodiversity, and increase overall farm productivity."
    }
  },
        "mango": {
        "selection of variety": {
        1: "Choose varieties like Alphonso, Dasheri, Kesar, or Himsagar based on region and market demand.",
        2: "Select grafted plants for better quality and uniform growth."
    },
    "site selection and soil preparation": {
        1: "Select a sunny location with well-drained loamy soil.",
        2: "Prepare pits of size 1m x 1m x 1m and fill with topsoil, compost, and farmyard manure."
    },
    "planting": {
        1: "Plant during the monsoon or early spring season for better establishment.",
        2: "Maintain a spacing of 8-10 meters between trees for proper growth.",
        3: "Water the plants immediately after planting."
    },
    "irrigation management": {
        1: "Water young plants regularly, especially during dry seasons.",
        2: "For mature trees, irrigate during flowering and fruiting stages to enhance yield."
    },
    "pruning and training": {
        1: "Remove dead, diseased, or weak branches periodically.",
        2: "Train young trees to develop a strong framework."
    },
    "fertilizer application": {
        1: "Apply farmyard manure (20-25 kg) and nitrogen, phosphorus, potassium (NPK) annually.",
        2: "Split fertilizer application into 2-3 doses during pre-flowering and post-harvest periods."
    },
    "pest and disease control": {
        1: "Monitor for common pests like mango hoppers, fruit flies, and mealybugs.",
        2: "Use neem oil, biopesticides, or eco-friendly traps for pest control.",
        3: "Prevent diseases like powdery mildew and anthracnose by using fungicides."
    },
    "flowering and pollination": {
        1: "Ensure good pollination by maintaining insect-friendly habitats.",
        2: "Avoid excessive use of pesticides during flowering to protect pollinators."
    },
    "harvesting": {
        1: "Harvest fruits when they are fully mature, typically 3-5 months after flowering.",
        2: "Pick fruits carefully to avoid bruising and damage."
    },
    "post-harvest management": {
        1: "Sort and grade fruits based on size and quality.",
        2: "Store fruits in cool, ventilated areas to maintain freshness.",
        3: "Use proper packaging for transportation to avoid damage."
    }
    },
        "mothbean": {
    "variety selection": {
      1: "Choose drought-tolerant and heat-resistant varieties adapted to arid and semi-arid regions.",
      2: "Consider varieties with early maturity for short growing seasons and escape drought periods.",
      3: "Select varieties with high yield potential and desirable seed characteristics (e.g., seed size, color, and cooking quality).",
      4: "Look for varieties resistant to major pests and diseases prevalent in the region."
    },
    "site preparation": {
      1: "Mothbean thrives in well-drained sandy loam to loamy sand soils with a pH of 6.0-7.5.",
      2: "Avoid waterlogged or heavy clay soils, as they can lead to poor germination and root rot.",
      3: "Prepare a fine seedbed by plowing or harrowing 1-2 times followed by leveling to create a smooth and even surface.",
      4: "Incorporate well-rotted farmyard manure (FYM) or compost during land preparation to improve soil structure and water retention, especially in sandy soils."
    },
    "planting material": {
      1: "Use certified, disease-free seeds from reliable sources to ensure good germination and seedling vigor.",
      2: "Treat seeds with a fungicide (e.g., thiram or carbendazim) to protect against seedborne diseases and improve seedling establishment.",
      3: "Inoculate seeds with appropriate Rhizobium culture (specific to mothbean) to enhance nitrogen fixation and reduce the need for nitrogen fertilizers, especially in soils with low organic matter.",
      4: "Ensure good seed viability by conducting a germination test before sowing."
    },
    "planting": {
      1: "Sow seeds after the first monsoon showers or when sufficient soil moisture is available for germination.",
      2: "The optimal sowing time varies depending on the region and rainfall patterns.",
      3: "Use a seed drill or sow manually in rows with a spacing of 30-45 cm between rows and 10-15 cm between plants within a row.",
      4: "Sow seeds at a shallow depth of 2-3 cm to ensure good emergence, especially in dry conditions.",
      5: "Maintain a plant population of approximately 30-40 plants per square meter for optimal yield."
    },
    "irrigation": {
      1: "Mothbean is known for its drought tolerance and is primarily grown as a rainfed crop in arid and semi-arid regions.",
      2: "Supplemental irrigation can significantly increase yields, especially during critical growth stages like flowering and pod filling, if water is available.",
      3: "Avoid overwatering, as it can lead to root rot and other diseases, especially in poorly drained soils.",
      4: "Use efficient irrigation methods like furrow or sprinkler irrigation if supplemental irrigation is practiced."
    },
    "nutrient management": {
      1: "Apply a basal dose of FYM or compost during land preparation to improve soil organic matter and nutrient availability.",
      2: "Apply recommended doses of phosphorus (P) and potassium (K) fertilizers based on soil test results.",
      3: "Nitrogen fertilizer is generally not required if seeds are properly inoculated with Rhizobium, as mothbean is a legume and fixes atmospheric nitrogen.",
      4: "If nitrogen deficiency is observed (pale green leaves), a small dose of nitrogen fertilizer can be applied as a top dressing.",
      5: "Avoid excessive nitrogen application, as it can promote vegetative growth at the expense of pod setting and seed yield."
    },
    "weed control": {
      1: "Weed control is important during the initial growth stages of mothbean to prevent competition for limited resources like water and nutrients.",
      2: "Perform 1-2 hand weedings or use pre-emergence or post-emergence herbicides to control weeds effectively.",
      3: "Intercultural operations like hoeing can also help in weed control and improve soil aeration.",
      4: "Maintain a clean field to minimize weed pressure and maximize yield, especially in water-scarce environments."
    },
    "pest control": {
      1: "Monitor for common mothbean pests such as aphids, pod borers, and hairy caterpillars.",
      2: "Use integrated pest management (IPM) strategies, including cultural, biological, and chemical methods, to manage pests effectively and minimize environmental impact.",
      3: "Use recommended insecticides judiciously when pest populations reach economic threshold levels.",
      4: "Encourage natural enemies of pests like ladybugs and lacewings to provide natural pest control."
    },
    "disease management": {
      1: "Mothbean is relatively resistant to many diseases, but some fungal diseases like leaf spots and root rots can occur under favorable conditions.",
      2: "Plant disease-resistant varieties whenever possible to minimize disease incidence.",
      3: "Practice crop rotation to break disease cycles and reduce pathogen buildup in the soil.",
      4: "Ensure good drainage to prevent waterlogging, which can promote root rot.",
      5: "Use recommended fungicides for disease control if necessary, following label instructions carefully."
    },
    "harvesting": {
      1: "Harvest mothbean when the pods are dry and turn yellowish-brown or light brown and the seeds are mature and hard.",
      2: "Harvesting can be done manually by uprooting the plants or by picking the mature pods.",
      3: "Dry the harvested plants or pods in the sun for a few days to reduce moisture content before threshing.",
      4: "Thresh the dried plants or pods to separate the seeds from the pods and other plant debris."
    },
    "post-harvest": {
      1: "Clean the harvested seeds to remove debris, broken seeds, and other impurities.",
      2: "Dry the cleaned seeds to a safe moisture level (around 8-10%) to prevent storage losses due to mold and insect infestation.",
      3: "Store the dried seeds in clean, dry, and airtight containers or bags in a cool and dry place, protected from pests and rodents.",
      4: "Fumigate stored seeds if necessary to control storage pests."
    },
    "crop rotation": {
      1: "Rotate mothbean with non-leguminous crops like cereals (e.g., pearl millet, sorghum) to improve soil fertility and reduce pest and disease buildup.",
      2: "Avoid continuous cropping of legumes in the same field.",
      3: "Include mothbean in crop rotation systems to enhance soil health, improve biodiversity, and increase overall farm productivity in dryland farming systems."
    }
  }, 
        "pomegranate": {
    "variety selection": {
      1: "Choose varieties adapted to your climate (e.g., 'Wonderful' for warm climates, others for cooler regions).",
      2: "Consider fruit characteristics like color, size, sweetness, and seed hardness (soft-seeded varieties are available).",
      3: "Select for disease resistance, particularly to fruit rot and bacterial blight."
    },
    "site preparation": {
      1: "Pomegranates prefer well-drained sandy loam soil with a pH of 6.0-7.0.",
      2: "Ensure the site receives full sun (at least 6-8 hours per day).",
      3: "Prepare the soil by deep plowing or digging to improve drainage and root penetration.",
      4: "Incorporate organic matter like compost or well-rotted manure to enhance soil fertility."
    },
    "planting material": {
      1: "Use healthy, disease-free cuttings or one- to two-year-old nursery-grown trees.",
      2: "Cuttings should be taken from mature, healthy branches during the dormant season.",
      3: "Bare-root trees should be planted during the dormant season, while container-grown trees can be planted year-round (avoiding extreme heat or cold)."
    },
    "planting": {
      1: "Plant during the dormant season (late fall or early spring) in most climates.",
      2: "Dig holes slightly larger than the root ball and space trees 15-20 feet apart.",
      3: "Plant at the same depth the tree was growing in the nursery.",
      4: "Water thoroughly after planting and apply mulch to conserve moisture and suppress weeds."
    },
    "irrigation": {
      1: "Pomegranates are relatively drought-tolerant once established, but regular watering is crucial during the first few years and during fruit development.",
      2: "Water deeply and less frequently rather than shallowly and often.",
      3: "Use drip irrigation or soaker hoses to deliver water directly to the root zone and minimize foliar diseases.",
      4: "Reduce watering as fruit ripens to prevent fruit cracking."
    },
    "nutrient management": {
      1: "Apply a balanced fertilizer in early spring before new growth begins.",
      2: "Supplement with organic fertilizers like compost or manure throughout the growing season.",
      3: "Monitor for nutrient deficiencies and adjust fertilization accordingly.",
      4: "Avoid excessive nitrogen fertilization, which can promote vegetative growth at the expense of fruit production."
    },
    "pruning": {
      1: "Prune young trees to establish a strong framework of 3-5 main branches.",
      2: "Remove dead, damaged, and crossing branches annually during the dormant season.",
      3: "Prune to maintain an open canopy for good air circulation and sunlight penetration.",
      4: "Remove suckers that grow from the base of the tree."
    },
    "pest control": {
      1: "Monitor for common pomegranate pests such as aphids, mealybugs, and fruit borers.",
      2: "Use integrated pest management (IPM) strategies, including cultural practices, biological controls, and targeted insecticide applications if necessary.",
      3: "Protect ripening fruit from birds and other wildlife using netting or other deterrents."
    },
    "disease management": {
      1: "Watch for common pomegranate diseases such as fruit rot (caused by various fungi) and bacterial blight.",
      2: "Practice good sanitation by removing fallen fruit and leaves.",
      3: "Ensure good air circulation through proper pruning and spacing.",
      4: "Apply appropriate fungicides or bactericides if necessary, following label instructions carefully."
    },
    "harvesting": {
      1: "Harvest pomegranates when they are fully colored, develop a metallic sound when tapped, and the skin becomes slightly thinner.",
      2: "Clip or cut the fruit from the tree, leaving a short stem attached.",
      3: "Avoid bruising the fruit during harvest."
    },
    "post-harvest": {
      1: "Store pomegranates in a cool, dry place for several weeks or in the refrigerator for up to several months.",
      2: "Handle fruit carefully to prevent bruising during storage and transport.",
      3: "Pomegranates can be juiced, seeded, or used in various culinary applications."
    }
  },
        "kidneybean": {
    "variety selection": {
      1: "Choose varieties adapted to your climate (bush or pole types). Bush types are self-supporting, while pole types require trellising.",
      2: "Select for disease resistance, especially to common bean mosaic virus (CBMV), anthracnose, and bacterial blights.",
      3: "Consider the intended use (dry beans or snap beans/green beans).",
      4: "Select for desired seed characteristics (size, shape, color) and maturity time (early, mid, or late season)."
    },
    "site preparation": {
      1: "Kidney beans prefer well-drained, fertile loam or sandy loam soil with a pH of 6.0-7.0.",
      2: "Avoid heavy clay soils that retain water.",
      3: "Prepare the soil by plowing or tilling to a depth of 8-10 inches to create a loose and friable seedbed.",
      4: "Incorporate well-rotted compost or manure to improve soil fertility and drainage.",
      5: "Ensure the site receives at least 6-8 hours of sunlight per day."
    },
    "planting material": {
      1: "Use certified, disease-free seeds from reputable sources.",
      2: "Inoculate seeds with Rhizobium bacteria to enhance nitrogen fixation (especially important in soils that haven't grown beans recently).",
      3: "Avoid using seeds saved from previous crops if there's a risk of disease transmission."
    },
    "planting": {
      1: "Plant after the last frost when the soil temperature is consistently above 50°F (10°C).",
      2: "Direct sow seeds 1-2 inches deep and 2-4 inches apart in rows 18-24 inches apart for bush types.",
      3: "For pole beans, plant seeds 4-6 inches apart at the base of a trellis or other support structure.",
      4: "Water gently after planting to ensure good seed-to-soil contact.",
      5: "Avoid planting in cold, wet soil, as this can lead to seed rot."
    },
    "irrigation": {
      1: "Provide consistent moisture, especially during flowering and pod development.",
      2: "Water deeply and less frequently rather than shallowly and often.",
      3: "Avoid overhead watering to reduce the risk of foliar diseases.",
      4: "Use soaker hoses or drip irrigation if possible.",
      5: "Allow the soil surface to dry slightly between waterings."
    },
    "nutrient management": {
      1: "Kidney beans are legumes and can fix nitrogen from the atmosphere, so excessive nitrogen fertilization is generally not needed.",
      2: "Apply phosphorus and potassium based on soil test recommendations.",
      3: "Incorporate compost or well-rotted manure before planting to provide essential nutrients.",
      4: "Avoid applying high-nitrogen fertilizers, as this can promote excessive vegetative growth and reduce pod production."
    },
    "weed control": {
      1: "Control weeds regularly, especially during the early growth stages.",
      2: "Hand weeding or shallow cultivation can be effective.",
      3: "Mulching can help suppress weeds and conserve soil moisture.",
      4: "Avoid deep cultivation, as this can damage bean roots."
    },
    "pest control": {
      1: "Monitor for common bean pests such as aphids, bean beetles, and spider mites.",
      2: "Use integrated pest management (IPM) strategies, including handpicking, insecticidal soap, or neem oil, if necessary.",
      3: "Encourage beneficial insects that prey on bean pests."
    },
    "disease management": {
      1: "Watch for common bean diseases such as anthracnose, bacterial blights, and white mold.",
      2: "Plant disease-resistant varieties whenever possible.",
      3: "Practice crop rotation to reduce disease buildup in the soil.",
      4: "Ensure good air circulation by spacing plants properly.",
      5: "Avoid overhead watering and remove infected plant debris promptly."
    },
    "harvesting": {
      1: "For dry beans, harvest when the pods are dry and brittle and the beans rattle inside.",
      2: "Pull up the entire plant and allow it to dry completely in a well-ventilated area.",
      3: "Thresh the dried pods to release the beans.",
      4: "For snap beans (green beans), harvest when the pods are young, tender, and before the beans inside fully develop.",
      5: "Pick snap beans regularly to encourage continuous production."
    },
    "post-harvest": {
      1: "For dry beans, clean the harvested beans to remove debris and damaged beans.",
      2: "Dry the beans further if necessary to ensure proper storage.",
      3: "Store dry beans in airtight containers in a cool, dry place.",
      4: "Snap beans should be refrigerated and used within a few days of harvest."
    },
    "crop rotation": {
      1: "Rotate kidney beans with non-leguminous crops to improve soil health and reduce pest and disease problems.",
      2: "Avoid planting beans in the same location more than once every 2-3 years.",
      3: "Good rotation crops include corn, grains, and leafy greens."
    }
  },
        "chickpea": {
    "variety selection": {
      1: "Choose varieties adapted to your climate (desi or kabuli types). Desi types are smaller, darker, and have a rough coat, while kabuli types are larger, lighter-colored, and have a smoother coat.",
      2: "Select for disease resistance, especially to Ascochyta blight, Fusarium wilt, and root rots."
    },
    "site preparation": {
      1: "Chickpeas prefer well-drained, light to medium textured soils with a pH of 6.0-7.0.",
      2: "Prepare a fine seedbed by plowing or harrowing followed by leveling to ensure good seed-soil contact."
    },
    "planting material": {
      1: "Use certified, disease-free seeds from reputable sources.",
      2: "Inoculate seeds with Rhizobium bacteria to enhance nitrogen fixation."
    },
    "planting": {
      1: "Plant after the last frost in spring or in the fall in warmer climates.",
      2: "Direct sow seeds 2-3 inches deep and 4-6 inches apart in rows 18-24 inches apart."
    },
    "irrigation": {
      1: "Chickpeas are relatively drought-tolerant but benefit from irrigation during critical growth stages like flowering and pod filling.",
      2: "Avoid overwatering, as it can lead to root rot."
    },
    "nutrient management": {
      1: "Apply phosphorus and potassium based on soil test recommendations.",
      2: "Avoid excessive nitrogen fertilization, as it can promote vegetative growth and reduce pod production."
    },
    "weed control": {
      1: "Control weeds regularly, especially during the early growth stages.",
      2: "Hand weeding or shallow cultivation can be effective."
    },
    "pest control": {
      1: "Monitor for common chickpea pests such as pod borers and aphids.",
      2: "Use integrated pest management (IPM) strategies as needed."
    },
    "disease management": {
      1: "Watch for common chickpea diseases such as Ascochyta blight, Fusarium wilt, and root rots.",
      2: "Plant disease-resistant varieties and practice crop rotation."
    },
    "harvesting": {
      1: "Harvest when the pods are dry and turn brown and the plants begin to yellow.",
      2: "Pull up the entire plant and allow it to dry completely before threshing."
    },
    "post-harvest": {
      1: "Clean the harvested chickpeas to remove debris and damaged seeds.",
      2: "Store dry chickpeas in airtight containers in a cool, dry place."
    },
    "crop rotation": {
      1: "Rotate chickpeas with non-leguminous crops to improve soil health and reduce pest and disease problems.",
      2: "Avoid planting chickpeas in the same location more than once every 2-3 years."
    }
  }, 
        "coffee": {
    "variety selection": {
      1: "Choose varieties adapted to your climate and altitude (Arabica, Robusta, Liberica, Excelsa). Arabica prefers higher altitudes and cooler temperatures, while Robusta thrives in hotter, lower-lying areas.",
      2: "Consider disease resistance, yield potential, and cup quality (flavor and aroma)."
    },
    "site preparation": {
      1: "Select a site with well-drained soil, rich in organic matter, and a slightly acidic pH (5.5-6.5).",
      2: "Provide adequate shade, especially for Arabica, using shade trees or artificial shade structures.",
      3: "Clear the land of weeds and debris and prepare planting holes."
    },
    "planting material": {
      1: "Use healthy, disease-free seedlings or cuttings from reputable nurseries.",
      2: "Select seedlings that are 6-12 months old and have a well-developed root system."
    },
    "planting": {
      1: "Plant during the rainy season to ensure adequate moisture for establishment.",
      2: "Plant seedlings in prepared holes, ensuring the root ball is level with the ground surface.",
      3: "Space plants according to the variety and growing system (typically 1-2 meters apart)."
    },
    "irrigation": {
      1: "Coffee requires consistent moisture, especially during dry periods and flowering/fruiting stages.",
      2: "Irrigate regularly, but avoid overwatering, which can lead to root rot.",
      3: "Use efficient irrigation methods like drip or sprinkler irrigation."
    },
    "nutrient management": {
      1: "Apply organic manure or compost regularly to improve soil fertility.",
      2: "Use balanced fertilizers containing nitrogen, phosphorus, and potassium, as well as micronutrients.",
      3: "Apply fertilizers in split doses throughout the year, especially during periods of active growth and fruit development."
    },
    "pruning": {
      1: "Prune regularly to maintain tree shape, improve air circulation, and promote fruit production.",
      2: "Remove dead, damaged, and diseased branches, as well as suckers and water sprouts.",
      3: "Use appropriate pruning techniques depending on the variety and growing system."
    },
    "pest control": {
      1: "Monitor for common coffee pests such as coffee berry borer, leaf miners, and mealybugs.",
      2: "Use integrated pest management (IPM) strategies, including cultural practices, biological controls, and targeted insecticide applications if necessary.",
      3: "Practice good sanitation by removing fallen berries and leaves."
    },
    "disease management": {
      1: "Watch for common coffee diseases such as coffee leaf rust, coffee berry disease, and root diseases.",
      2: "Plant disease-resistant varieties whenever possible.",
      3: "Practice good sanitation and ensure proper air circulation to reduce disease incidence.",
      4: "Use recommended fungicides for disease control if necessary."
    },
    "harvesting": {
      1: "Harvest coffee cherries when they are fully ripe and red (or yellow depending on the variety).",
      2: "Harvesting can be done manually by handpicking or mechanically using shakers.",
      3: "Harvest selectively, picking only ripe cherries to ensure high quality."
    },
    "post-harvest": {
      1: "Process harvested cherries promptly to prevent spoilage.",
      2: "Common processing methods include wet processing (washed coffee) and dry processing (natural coffee).",
      3: "Dry the processed beans to a specific moisture content before storage and export."
    },
    "shade management":{
      1: "Provide adequate shade to regulate temperature, reduce water stress, and create a favorable microclimate for coffee growth.",
      2: "Use diverse shade trees that provide multiple benefits, such as nitrogen fixation, soil improvement, and biodiversity conservation."
    }
  }
}
   
    data = request.get_json()
    crop_name = data.get("cropName", "").strip().lower()
    print(f"Received crop name: {crop_name}")  # Debug log

    if crop_name in my_dict:
        print(f"Crop details found for: {crop_name}")
        return jsonify({crop_name: my_dict[crop_name]})
    else:
        print(f"Crop details not found for: {crop_name}")
        return jsonify({"error": "Crop not found"}), 404
    
@app.route('/api/enviromentDetails',methods=['POST'])
def get_enviroment_details():
    my_enviro_dict={
        "rice":{
            "Temp":"26°c-30°c",
            "pH":"5-7",
            "Nitrogen":"60-70",
            "Phosphorus":"35-40",
            "Potassium":"35-40",
            "Rainfall":"182-200"
        },
        "maize":{
            "Temp":"18°c-26°c",
            "pH":"5-6.99",
            "Nitrogen":"60-100",
            "Phosphorus":"35-60",
            "Potassium":"15-25",
            "Rainfall":"182-200"
        },
        "chickpea":{
            "Temp":"17°c-20°c",
            "pH":"5-8",
            "Nitrogen":"20-60",
            "Phosphorus":"55-80",
            "Potassium":"75-85",
            "Rainfall":"65-94"
        },
        "kidneypea":{
            "Temp":"15°c-24°c",
            "pH":"5.5-5.9",
            "Nitrogen":"0-40",
            "Phosphorus":"55-80",
            "Potassium":"15-24",
            "Rainfall":"60-150"
        },
        "pigeonpea":{
            "Temp":"26°c-30°c",
            "pH":"5-7",
            "Nitrogen":"0-40",
            "Phosphorus":"55-80",
            "Potassium":"15-25",
            "Rainfall":"90-198"
        },
        "mothbean":{
            "Temp":"26°c-30°c",
            "pH":"3.5-9.9",
            "Nitrogen":"0-40",
            "Phosphorus":"35-60",
            "Potassium":"15-25",
            "Rainfall":"30-74"
        },
        "mungbean":{
            "Temp":"27°c-29°c",
            "pH":"6.2-7.1",
            "Nitrogen":"0-40",
            "Phosphorus":"35-60",
            "Potassium":"15-25",
            "Rainfall":"36-59"
        },
        "blackgram":{
            "Temp":"25°c-34°c",
            "pH":"6.5-7.7",
            "Nitrogen":"20-60",
            "Phosphorus":"55-80",
            "Potassium":"15-25",
            "Rainfall":"60-74"
        },
        "lentil":{
            "Temp":"18°c-30°c",
            "pH":".95-7.8",
            "Nitrogen":"0-40",
            "Phosphorus":"55-80",
            "Potassium":"15-25",
            "Rainfall":"35-54"
        },
        "pomegnanate":{
            "Temp":"18°c-24°c",
            "pH":"5-7",
            "Nitrogen":"0-40",
            "Phosphorus":"5-30",
            "Potassium":"35-45",
            "Rainfall":"102-112"
        },
        "mango":{
            "Temp":"27°c-35°c",
            "pH":"4.5-6.9",
            "Nitrogen":"0-40",
            "Phosphorus":"15-40",
            "Potassium":"25-35",
            "Rainfall":"89-100"
        },
        "banana":{
            "Temp":"25°c-29°c",
            "pH":"5.5-6.4",
            "Nitrogen":"80-120",
            "Phosphorus":"70-95",
            "Potassium":"45-55",
            "Rainfall":"90-119"
        },
        "grapes":{
            "Temp":"8°c-41°c",
            "pH":"5.4-6.4",
            "Nitrogen":"0-40",
            "Phosphorus":"120-145",
            "Potassium":"195-205",
            "Rainfall":"65-74"
        },
        "watermelon":{
            "Temp":"24°c-26°c",
            "pH":"6-6.9",
            "Nitrogen":"80-120",
            "Phosphorus":"45-55",
            "Potassium":"35-40",
            "Rainfall":"40-59"
        },
        "muskmelon":{
            "Temp":"24°c-26°c",
            "pH":"6-6.9",
            "Nitrogen":"80-120",
            "Phosphorus":"5-30",
            "Potassium":"45-55",
            "Rainfall":"40-60"
        },
        "apple":{
            "Temp":"21°c-23°c",
            "pH":"5.5-6.4",
            "Nitrogen":"0-40",
            "Phosphorus":"120-145",
            "Potassium":"195-205",
            "Rainfall":"100-124"
        },
        "orange":{
            "Temp":"10°c-34°c",
            "pH":"6-7.9",
            "Nitrogen":"0-40",
            "Phosphorus":"5-30",
            "Potassium":"5-15",
            "Rainfall":"100-119"
        },
        "papaya":{
            "Temp":"23°c-43°c",
            "pH":"6.5-6.9",
            "Nitrogen":"60-70",
            "Phosphorus":"46-70",
            "Potassium":"45-55",
            "Rainfall":"40-248"
        },
        "coconut":{
            "Temp":"25°c-30°c",
            "pH":"5.5-6.4",
            "Nitrogen":"0-40",
            "Phosphorus":"5-30",
            "Potassium":"25-35",
            "Rainfall":"131-225"
        },
        "cotton":{
            "Temp":"22°c-25°c",
            "pH":"5.8-7.9",
            "Nitrogen":"100-140",
            "Phosphorus":"35-60",
            "Potassium":"15-25",
            "Rainfall":"60-90"
        },
        "jute":{
            "Temp":"23°c-26°c",
            "pH":"6-7.4",
            "Nitrogen":"60-100",
            "Phosphorus":"35-60",
            "Potassium":"35-45",
            "Rainfall":"150-199"
        },
        "coffee":{
            "Temp":"23°c-27°c",
            "pH":"6-7.4",
            "Nitrogen":"80-120",
            "Phosphorus":"15-40",
            "Potassium":"25-35",
            "Rainfall":"115-199"
        },

    }
    data=request.get_json()
    crop_name=data.get("cropName").lower()
    if crop_name in my_enviro_dict:
        return jsonify({crop_name:my_enviro_dict[crop_name]})
    else:
        return jsonify({"error": "Crop not found"}),404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
