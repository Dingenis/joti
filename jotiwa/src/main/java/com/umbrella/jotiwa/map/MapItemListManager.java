package com.umbrella.jotiwa.map;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by stesi on 18-9-2015.
 */
public class MapItemListManager<T> {

    private Map<String, T> collections = new HashMap<>();

    public T newItem(String id, T t)
    {
        return collections.put(id, t);
    }

    public T getItem(String id)
    {
        return collections.get(id);
    }
}