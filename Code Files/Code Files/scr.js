// Promises  code
let p = new Promise((resolve, reject) => {
    let a = 1 + 1
    if (a == 2) {
        resolve('Success')
    } else {
        reject('Failed')
    }
})


p.then((message) => { console.log("this is in the then" + message) }).catch((message) => { console.log("it is in the catch" + message) })


//callback code
userleft = false
userWachingCatMeme = false

function watchTutorialCallback(callback, errorCallback) {
    if (userleft) {
        errorCallback({
            name: 'user left',
            message: ":("
        })
    }
    else if (userWachingCatMeme) {
        errorCallback({
            name: 'user watching cat meme',
            message: 'webdevSimplified < Cat'
        })
    } else {
        callback('subscribe')
    }
}

watchTutorialCallback((message) => {
    console.log("success " + message)
}, (error) => {
    console.log(error.name + " " + error.message)
})



// running multiple promises at the same time

const recordOne = new Promise((resolve, reject) => {
    resolve('video 1 recorded')
})

const recordTwo = new Promise((resolve, reject) => {
    resolve('video 2 recorded')
})

const recordThree = new Promise((resolve, reject) => {
    resolve('video 3 recorded')
})

Promise.all([
    recordOne,
    recordTwo,
    recordThree
]).then((messages) => {
    console.log(messages)
})