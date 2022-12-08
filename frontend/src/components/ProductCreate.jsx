export const ProductCreate = () => {
    return (
        <form className="mt-3">
            <div className="form-floating pb-3">
                <input className="form-control" type="text" placeholder="Name" />
                <label>Name</label>
            </div>

            <div className="form-floating pb-3">
                <input
                    type="number"
                    className="form-control"
                    placeholder="Price"
                />
                <label>Price</label>
            </div>

            <div className="form-floating pb-3">
                <input
                    type="number"
                    className="form-control"
                    placeholder="Quantity"
                />
                <label>Quantity</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">
                Submit
            </button>
        </form>
    );
};
