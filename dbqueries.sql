call get_restaurant_order("43ee5692a7b44a798c3b8a095e3c7c61",true,true);
call get_client_order("randomfaketoken1",true,true);
call new_client_order("randomfaketoken1","[2,3,2]",2);
call client_edit("randomfaketoken1","changed","changed","changed","changed","changed","changed");

select convert(o.is_complete using "utf8")as is_complete,convert(o.is_confirmed using "utf8")as is_confirmed,
		convert(mi.name using "utf8")as name,convert(mi.price using "utf8")as price,
		convert(omi.menu_item_id using "utf8")as menu_item,convert(omi.order_id using "utf8")as order_id
		from foodie.order_menu_item omi inner join foodie.`order`o on o.id=order_id 
		inner join menu_item mi on mi.id=omi.menu_item_id where o.is_complete = true and o.client_id=(select client_id from client_session where token="randomfaketoken1");
	
call get_client_order("randomfaketoken1",t  rue,true);

select convert(o.is_complete using "utf8")as is_complete,convert(o.is_confirmed using "utf8")as is_confirmed,
		convert(mi.name using "utf8")as name,convert(mi.price using "utf8")as price,
		convert(omi.menu_item_id using "utf8")as menu_item,convert(omi.order_id using "utf8")as order_id
		from foodie.order_menu_item omi inner join foodie.`order`o on o.id=order_id 
		inner join menu_item mi on mi.id=omi.menu_item_id where o.client_id=(select client_id from client_session where token="randomfaketoken1")
		and o.is_complete = true;
		