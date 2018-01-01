package com.example.adityavats.bitsandpizzas;

import android.app.ListFragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
public class PastaFragmentFragment extends ListFragment {
  /**  ListFragmentItemClickListener ifaceItemClickListener;
    /** An interface for defining the callback method */
   // public interface ListFragmentItemClickListener {
        /** This method will be invoked when an item in the ListFragment is clicked */
     //   void onListFragmentItemClick(int position);
    //}
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(
                inflater.getContext(),
                android.R.layout.simple_list_item_1,
                getResources().getStringArray(R.array.pasta));
        setListAdapter(adapter);
        return super.onCreateView(inflater, container, savedInstanceState);
    }
//@Override
  //  public void onListItemClick(ListView l, View v, int position, long id){
    //super.onListItemClick(l, v, position, id);
    /** Invokes the implementation of the method onListFragmentItemClick in the hosting activity */
    //ifaceItemClickListener.onListFragmentItemClick(position);

}

//               }
