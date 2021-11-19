// movie class name, genere, OTT

class Movie{
    constructor(name, genere, ott){
        this.name = name
        this.genere = genere
        this.ott = ott
    }
}

// UI operations

class UI{
    static displayMovie(){
        const movies = [
            {
                name: "John Wick",
                genere: "Action",
                ott: "Netflix"
            },
            {
                name: "Avengers",
                genere: "Fantasy",
                ott: "Hotstar"
            },
            {
                name: "Conjuring",
                genere: "Horror",
                ott: "Amazon Prime"
            }
        ]
        movies.forEach(movie => UI.addMovieToList(movie))
    }

    static addMovieToList(movie){
        const list = document.getElementById('anime-list')
        const row = document.createElement('tr')
        row.innerHTML = `
        <td>${movie.name}</td>
        <td>${movie.genere}</td>
        <td>${movie.ott}</td>
        <td><a href="#" id = "delete">X</a></td>
        `
        list.appendChild(row)
    }

    static clearFields(){
        document.getElementById("name").value= ''
        document.getElementById("genere").value= ''
        document.getElementById("ott").value = ''
    }

    static deleteMovie(m){
        if(document.getElementById("delete")){
            m.parentElement.parentElement.remove()
            //console.log(m.parentElement.parentElement)
        }
    }
}


// display a movie

document.addEventListener('DOMContentLoaded', UI.displayMovie)


// adding a movie

document.addEventListener('submit', function(e){
    e.preventDefault()

    const name = document.querySelector('#name').value 
    const genere = document.querySelector('#genere').value 
    const ott = document.querySelector('#ott').value 

    if (name === "" || genere === "" || ott === ""){
        alert("Please enter all values")
    }
    else{
        const movie = new Movie(name, genere, ott)
        UI.addMovieToList(movie)
        UI.clearFields()
    }

})

// remove a movie
document.querySelector('#anime-list').addEventListener('click', function(e){
    UI.deleteMovie(e.target)
})