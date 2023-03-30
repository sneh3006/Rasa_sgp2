const mongoose = require("mongoose");
require('dotenv').config({path: './.env'})

mongoose.connect("mongodb+srv://sneh:Sneh1234@cluster0.vtybwdu.mongodb.net/?retryWrites=true&w=majority" , {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(()=> { 
    console.log('MongoDB connected');
}).catch((ERR) => {
    console.log('DB Connection Error');
    console.log(ERR);
})

const contactSchema = {
    email: String,
    username: String
 }; 
 