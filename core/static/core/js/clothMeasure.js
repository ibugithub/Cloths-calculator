const lenBtn  = document.getElementById('lenbtn')
const prizeSpace = document.getElementById('prizeSpace')
const rateWarning = document.getElementById('rateWarning')
const clearBtn = document.getElementById('clearbtn')
lenBtn.addEventListener("click", lenBtnFunc)
clearBtn.addEventListener('click', clearScreen)

// For getting the value form the input....
function lenBtnFunc(){
    let gozLenValue = document.getElementById('gozLenVal').value;
    let giraLenValue = document.getElementById('giraLenVal').value;
    let rateValue = document.getElementById('rateVal').value;

    $.ajax({
        type: "GET",
        url :'totalInfo/',
        
        success: function(data) {

            if (giraLenValue == ""){
                giraLenValue = 0
            }
            if (gozLenValue == ""){
                gozLenValue = 0
            }
            gozLenValue = parseFloat(gozLenValue)
            giraLenValue = parseFloat(giraLenValue) / 16
        
            if (rateValue == "")
            {   
                rateWarning.style.display = "block"
                rateWarning.innerHTML = "কাপরের রেট দেয়া হয় নি"
            }
            else 
            {   
                rateValue = parseFloat(rateValue)
                prizeSpace.innerHTML = ( (gozLenValue + giraLenValue) * rateValue) + data.totalPrize
                document.getElementById("totalInfo").style.display = "block"
            }
        }
    })
}


// For removing the ratewarning and prvious totalamount info..... 
const allInput = document.querySelectorAll(".input")
allInput.forEach(input => {
 input.addEventListener("change", function()
 {
     rateWarning.style.display = "none"
     document.getElementById("totalInfo").style.display = "none"
 })
});


// For removing the existing value in all input when aro ache button wil be  clicked
const aroAcheBtn = document.getElementById('aroAche')
aroAcheBtn.addEventListener('click',function(){
    console.log("The aro ache button has been clicked")
    let gozLen = document.getElementById('gozLenVal').value
    let giraLen = document.getElementById('giraLenVal').value
    let rate = document.getElementById('rateVal').value
    clearScreen()
    $.ajax({
        type: "GET",
        url: "/prevAmount",
        data : {
            gozLenV : gozLen,
            giraLenV : giraLen,
            rateV : rate
        },
        success : function(data){
            if (data.warning == 'rate'){
                rateWarning.style.display = "block"
                rateWarning.innerHTML = "কাপরের রেট দেয়া হয় নি"
            }
        }
    })
});



// This function will  clear the screen 
function clearScreen(){
    document.getElementById('gozLenVal').value = ''
    document.getElementById('giraLenVal').value = ''
    document.getElementById('rateVal').value = ''
    document.getElementById('totalInfo').style.display = 'none'
}