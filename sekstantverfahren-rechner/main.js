import './style.css'

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCQJk-go_4QSKFTVa9MbXDyuGdZ0y5dKlw",
  authDomain: "st-try-96e9c.firebaseapp.com",
  projectId: "st-try-96e9c",
  storageBucket: "st-try-96e9c.appspot.com",
  messagingSenderId: "396159879159",
  appId: "1:396159879159:web:9b32d5d13b2822474250f2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


document.getElementById("calculatebutton").addEventListener("click", () => {
  var value =  document.getElementById("inputform").value
  console.log(value)

})

