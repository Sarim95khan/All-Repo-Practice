'use client';

import { FC } from 'react';

const AButton = ({
  count,
  onClick,
}: {
  count: number;
  onClick: () => void;
}) => {
  return (
    <button
      onClick={onClick}
      className="text-2xl p-4 font-bold bg-blue-700 text-white hover:bg-blue-300"
    >
      Click me {count}
    </button>
  );
};

export default AButton;
