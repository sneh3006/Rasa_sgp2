const mongoose = require("mongoose");
require('dotenv').config({path: './.env'})

mongoose.connect(process.env.MONGO_URI , {
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
 