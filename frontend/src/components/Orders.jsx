import { useState } from "react";

export const Orders = () => {
    const [order, setOrder] = useState({
        product_id: "",
        quantity: "",
    });

    const [total, setTotal] = useState(null);

    const submitHandler = async (e) => {
        e.preventDefault();
        const response = await fetch("http://localhost:8001/orders", {
            method: "POST",
            headers: {
                "Content-Type": "Application/json",
            },
            body: JSON.stringify(order),
        });
        if (response.ok) {
            const responseProduct = await fetch(
                `http://localhost:8000/products/${order.product_id}`
            );
            const product = await responseProduct.json();
            setTotal(product["price"] * parseFloat(order.quantity) * 1.2);

            setOrder({
                price: "",
                product_id: "",
            });
        }
    };

    const changeHandler = (e) => {
        setOrder((order) => ({ ...order, [e.target.name]: e.target.value }));
    };

    return (
        <div className="container">
            <main>
                <div className="py-5 text-center">
                    <h2>Checkout form</h2>
                    <p className="lead"></p>
                    {total !== null ? (
                        <h3>
                            Your order created successful, total price is{" "}
                            {total}
                        </h3>
                    ) : null}
                </div>

                <form onSubmit={(e) => submitHandler(e)}>
                    <div className="row g-3">
                        <div className="col-sm-6">
                            <label className="form-label">Product</label>
                            <input
                                className="form-control"
                                name="product_id"
                                value={order.product_id}
                                onChange={(e) => changeHandler(e)}
                                required
                            />
                        </div>

                        <div className="col-sm-6">
                            <label className="form-label">Quantity</label>
                            <input
                                type="number"
                                className="form-control"
                                name="quantity"
                                value={order.quantity}
                                onChange={(e) => changeHandler(e)}
                                required
                            />
                        </div>
                    </div>
                    <hr className="my-4" />
                    <button
                        className="w-100 btn btn-primary btn-lg"
                        type="submit"
                    >
                        Buy
                    </button>
                </form>
            </main>
        </div>
    );
};
