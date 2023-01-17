program Example;

function Add(x, y: Integer): Integer;
begin
  Add := x + y
end;

function Add(s, t: string): string;
begin
  Add := Concat(s, t);
end;

begin
  WriteLn(Add(1, 2));
  WriteLn(Add('Hello, ', 'World!'));
end.