exports.esrever = function (list) {
  const size = list.length;
  for (let i = 0; i < size / 2; i++) {
    const temp = list[i];
    list[i] = list[size - i - 1];
    list[size - i] = temp;
  }
  return list;
};
