
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '80A0A1A3DCA94C95F15E3861A4690A97'
    
_lr_action_items = {')':([2,8,9,10,11,12,13,],[-6,13,-1,-3,-2,-4,-5,]),'(':([0,3,4,5,6,7,],[3,3,3,3,3,3,]),'+':([1,2,8,9,10,11,12,13,],[4,-6,4,-1,-3,-2,-4,-5,]),'*':([1,2,8,9,10,11,12,13,],[5,-6,5,5,-3,5,-4,-5,]),'-':([1,2,8,9,10,11,12,13,],[6,-6,6,-1,-3,-2,-4,-5,]),'NUMBER':([0,3,4,5,6,7,],[2,2,2,2,2,2,]),'/':([1,2,8,9,10,11,12,13,],[7,-6,7,7,-3,7,-4,-5,]),'$end':([1,2,9,10,11,12,13,],[0,-6,-1,-3,-2,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,3,4,5,6,7,],[1,8,9,10,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr + expr','expr',3,'p_expr','shelf.py',43),
  ('expr -> expr - expr','expr',3,'p_expr','shelf.py',44),
  ('expr -> expr * expr','expr',3,'p_expr','shelf.py',45),
  ('expr -> expr / expr','expr',3,'p_expr','shelf.py',46),
  ('expr -> ( expr )','expr',3,'p_expr_paren','shelf.py',52),
  ('expr -> NUMBER','expr',1,'p_expr_number','shelf.py',57),
]