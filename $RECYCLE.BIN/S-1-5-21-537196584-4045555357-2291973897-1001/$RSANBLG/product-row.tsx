const ProductRow = ({ product }: { product: any }) => {
  const name = product.stocked ? (
    product.name
  ) : (
    <span className="bg-red-400">{product.name}</span>
  );
  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
};

export default ProductRow;
