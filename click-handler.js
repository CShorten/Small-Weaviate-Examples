function handleImageClick(data) {
        console.log(data);
        fetch("/image-clicked", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ imagePath: data })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
              }
              return response.json();
        })
        .then(data => {
            // Handle the response from the Python controller
            // Update the image elements on the page with the new image paths
            const imageCells = document.querySelectorAll(".image-cell");
            console.log(data);
            const newData = data["data"];
            //const image_dict = data["image_dict"];
            const userClicks = new Set(data["user_clicks"]);
            imageCells.forEach((cell, index) => {
                const image = cell.querySelector("img");
                //const imagePath = data.image_dict["image"+String(index)];
                const imagePath = newData[index]["image_path"];
                const distance = newData[index]["distance"];
                image.src = "/static/" + imagePath;
                image.id = imagePath;
    
                // Update the h2 element with the new image path
                const h2Element = cell.querySelector("h2");
                h2Element.textContent = "Distance to centroid: " + distance;
    
                console.log(userClicks.has(image.id));
                if (userClicks.has(image.id)) {
                    image.classList.add("clicked-image");
                } else {
                    image.classList.remove("clicked-image")
                }
                
                const oldClickListener = image.listener; // Retrieve the reference to the old listener
                image.removeEventListener("click", oldClickListener);
                const newClickListener = createClickListener(image);
                image.addEventListener("click", newClickListener);
                image.listener = newClickListener; // Store the reference to the new listener
            });
        })
        .catch(error => {
            console.error(error);
        });
    
    }
