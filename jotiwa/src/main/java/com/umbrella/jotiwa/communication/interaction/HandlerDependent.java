package com.umbrella.jotiwa.communication.interaction;

import android.os.Handler;

/**
 * Created by stesi on 22-9-2015.
 */
public class HandlerDependent {

    protected Handler handler;

    /**
     * @return
     */
    public Handler getHandler() {
        return handler;
    }

    /**
     * @param handler
     */
    public void setHandler(Handler handler) {
        this.handler = handler;
    }
}
