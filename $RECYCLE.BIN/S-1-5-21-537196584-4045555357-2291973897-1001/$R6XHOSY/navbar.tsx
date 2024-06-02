function AdminLogo() {
  return (
    <div>
      <p className="font-bold text-sm p-2">Sarim</p>
    </div>
  );
}

function UserLogo() {
  return (
    <div className="bg-slate-300 rounded-full">
      <p className="font-bold">Signin</p>
    </div>
  );
}

const Navbar = () => {
  const loggedIn = true;
  return (
    <div className="bg-white border-b h-16 flex items-center  px-10">
      <span>Logo</span>
      <div className="ml-auto bg-slate-300  rounded-full">
        {loggedIn ? <AdminLogo /> : <UserLogo />}
      </div>
    </div>
  );
};

export default Navbar;
