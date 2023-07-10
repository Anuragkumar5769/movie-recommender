// API Basic Configuration Object


var films=movies_name_list


const autoCompleteJS = new autoComplete(
    // API Advanced Configuration Object
{
    selector: "#autoComplete",
    placeHolder: "Search for Movies...",
    data: {
        src: films,
        cache: true,
    },
    resultsList: {
        element: (list, data) => {
            if (!data.results.length) {
                // Create "No Results" message element
                const message = document.createElement("div");
                // message.style.Color="white";
                // Add class to the created element
                message.setAttribute("class", "no_result");
                // Add message text content
                message.innerHTML = `<span style="color:powderblue;" >Found No Results for "${data.query}"</span>`;
                // Append message element to the results list
                list.prepend(message);
            }
        },
        noResults: true,
    },
    resultItem: {
        highlight: true,
    },
    events: {
        input: {
            selection: (event) => {
                const selection = event.detail.selection.value;
                autoCompleteJS.input.value = selection;
            }
        }
    },
    submit: true,
}

     );