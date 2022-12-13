import { useState } from "react";
import { useNavigate } from "react-router-dom";

export const ProductCreate = () => {
    const navigate = useNavigate();

    const [product, setProduct] = useState({
        name: "",
        price: "",
        quantity: "",
    });

    const submitHandler = async (e) => {
        e.preventDefault();
        const response = await fetch("http://localhost:8000/products", {
            method: "POST",
            headers: {
                "Content-Type": "Application/json",
            },
            body: JSON.stringify(product),
        });
        if (response.ok) {
            navigate(-1);
        }
    };

    const changeHandler = (e) => {
        setProduct((product) => ({
            ...product,
            [e.target.name]: e.target.value,
        }));
    };

    return (
        <form className="mt-3" onSubmit={(e) => submitHandler(e)}>
            <div className="form-floating pb-3">
                <input
                    className="form-control"
                    type="text"
                    placeholder="Name"
                    onChange={(e) => changeHandler(e)}
                    value={product.name}
                    name="name"
                    required
                />
                <label>Name</label>
            </div>

            <div className="form-floating pb-3">
                <input
                    type="number"
                    className="form-control"
                    placeholder="Price"
                    onChange={(e) => changeHandler(e)}
                    value={product.price}
                    name="price"
                    required
                />
                <label>Price</label>
            </div>

            <div className="form-floating pb-3">
                <input
                    type="number"
                    className="form-control"
                    placeholder="Quantity"
                    onChange={(e) => changeHandler(e)}
                    value={product.quantity}
                    name="quantity"
                    required
                />
                <label>Quantity</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">
                Submit
            </button>
        </form>
    );
};
