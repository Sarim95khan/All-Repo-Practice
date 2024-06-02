import Image from 'next/image';

const User = ['Sarim', 'Yahya', 'Hasan', 'Areeb'];

const user = {
  name: 'Hedy Lamarr',
  imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
  imageSize: 90,
};

const UserList = () => {
  return (
    <div className="pt-10 flex flex-col items-center justify-center w-full mx-auto">
      {User.map((user) => (
        <div className="bg-slate-400 px-4 flex flex-col space-y-4 border text-center">
          <p key={user}>{user}</p>
        </div>
      ))}

      <div className="relative mt-10 flex items-center justify-center bg-blue-300 rounded-lg p-2 shadow-sm hover:shadow-lg transition">
        <h1 className="font-bold">{user.name}</h1>
        <Image
          src={user.imageUrl}
          height={96}
          width={96}
          alt="Image"
          className="rounded-full ml-4"
        />
      </div>
    </div>
  );
};

export default UserList;
