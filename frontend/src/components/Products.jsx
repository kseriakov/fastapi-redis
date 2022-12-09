import { useEffect } from "react";
import { useState } from "react";
import { Link } from "react-router-dom";

export const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const abortCtrl = new AbortController();

        const getData = async () => {
            const response = await fetch("http://localhost:8000/products", {
                signal: abortCtrl.signal,
            });
            const productsData = await response.json();

            setProducts(productsData);
        };
        getData();

        return () => abortCtrl.abort();
    }, []);

    const deleteHandler = async (pk) => {
        await fetch(`http://localhost:8000/products/${pk}`, {
            method: "DELETE",
        });

        setProducts((products) => products.filter((item) => item.pk !== pk));
    };

    return (
        <div className="table-responsive">
            <div className="pt-3 pb-2 mb-3 border-bottom">
                <Link
                    to={"create"}
                    className="btn btn-sm btn-outline-secondary"
                >
                    Add product
                </Link>
            </div>
            <table className="table table-striped table-sm">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((item) => {
                        return (
                            <tr key={item.pk}>
                                {<td>{item.pk}</td>}
                                <td>{item.name}</td>
                                <td>{item.price}</td>
                                <td>{item.quantity}</td>
                                <td>
                                    <a
                                        href="#"
                                        className="btn btn-sm btn-outline-secondary"
                                        onClick={() => deleteHandler(item.pk)}
                                    >
                                        Delete
                                    </a>
                                </td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
};
